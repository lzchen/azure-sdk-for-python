#-------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#--------------------------------------------------------------------------
import functools
import inspect
import os.path
import sys
import zlib
try:
    from inspect import getfullargspec as get_arg_spec
except ImportError:
    from inspect import getargspec as get_arg_spec

import pytest

from azure_devtools.scenario_tests import (
    ReplayableTest, AzureTestError,
    GeneralNameReplacer, RequestUrlNormalizer,
    AuthenticationMetadataFilter, OAuthRequestResponsesFilter
)
from azure_devtools.scenario_tests.config import TestConfig
from azure_devtools.scenario_tests.utilities import trim_kwargs_from_test_function

from .config import TEST_SETTING_FILENAME
from . import mgmt_settings_fake as fake_settings


class HttpStatusCode(object):
    OK = 200
    Created = 201
    Accepted = 202
    NoContent = 204
    NotFound = 404


def get_resource_name(name_prefix, identifier):
    # Append a suffix to the name, based on the fully qualified test name
    # We use a checksum of the test name so that each test gets different
    # resource names, but each test will get the same name on repeat runs,
    # which is needed for playback.
    # Most resource names have a length limit, so we use a crc32
    checksum = zlib.adler32(identifier) & 0xffffffff
    name = '{}{}'.format(name_prefix, hex(checksum)[2:]).rstrip('L')
    if name.endswith('L'):
        name = name[:-1]
    return name


def get_qualified_method_name(obj, method_name):
    # example of qualified test name:
    # test_mgmt_network.test_public_ip_addresses
    _, filename = os.path.split(inspect.getsourcefile(type(obj)))
    module_name, _ = os.path.splitext(filename)
    return '{0}.{1}'.format(module_name, method_name)


def is_live():
    """A module version of is_live, that could be used in pytest marker.
    """
    if not hasattr(is_live, '_cache'):
        config_file = os.path.join(os.path.dirname(__file__), TEST_SETTING_FILENAME)
        if not os.path.exists(config_file):
            config_file = None
        is_live._cache = TestConfig(config_file=config_file).record_mode
    return is_live._cache


def get_region_override(default='westus'):
    region = os.environ.get('RESOURCE_REGION', None) or default
    if not region:
        raise ValueError('Region should not be None; set a non-empty-string region to either the RESOURCE_REGION environment variable or the default parameter to this function.')
    return region


def _is_autorest_v3(client_class):
    """ IS this client a autorestv3/track2 one?.
    Could be refined later if necessary.
    """
    args = get_arg_spec(client_class.__init__).args
    return "credential" in args


class AzureTestCase(ReplayableTest):
    def __init__(self, method_name, config_file=None,
                 recording_dir=None, recording_name=None,
                 recording_processors=None, replay_processors=None,
                 recording_patches=None, replay_patches=None,
                 **kwargs):
        self.working_folder = os.path.dirname(__file__)
        self.qualified_test_name = get_qualified_method_name(self, method_name)
        self._fake_settings, self._real_settings = self._load_settings()
        self.scrubber = GeneralNameReplacer()
        config_file = config_file or os.path.join(self.working_folder, TEST_SETTING_FILENAME)
        if not os.path.exists(config_file):
            config_file = None
        super(AzureTestCase, self).__init__(
            method_name,
            config_file=config_file,
            recording_dir=recording_dir,
            recording_name=recording_name or self.qualified_test_name,
            recording_processors=recording_processors or self._get_recording_processors(),
            replay_processors=replay_processors or self._get_replay_processors(),
            recording_patches=recording_patches,
            replay_patches=replay_patches,
            **kwargs
        )

    @property
    def settings(self):
        if self.is_live:
            if self._real_settings:
                return self._real_settings
            else:
                raise AzureTestError('Need a mgmt_settings_real.py file to run tests live.')
        else:
            return self._fake_settings

    def _load_settings(self):
        try:
            from . import mgmt_settings_real as real_settings
            return fake_settings, real_settings
        except ImportError:
            return fake_settings, None

    def _get_recording_processors(self):
        return [
            self.scrubber,
            AuthenticationMetadataFilter(),
            OAuthRequestResponsesFilter(),
            RequestUrlNormalizer()
        ]

    def _get_replay_processors(self):
        return [
            RequestUrlNormalizer()
        ]

    def is_playback(self):
        return not self.is_live

    def get_settings_value(self, key):
        key_value = os.environ.get("AZURE_"+key, None)

        if key_value and self._real_settings and getattr(self._real_settings, key) != key_value:
            raise ValueError("You have both AZURE_{key} env variable and mgmt_settings_real.py for {key} to difference values".format(key=key))

        if not key_value:
            try:
                key_value = getattr(self.settings, key)
            except Exception:
                print("Could not get {}".format(key))
                raise
        return key_value

    def set_value_to_scrub(self, key, default_value):
        if self.is_live:
            value = self.get_settings_value(key)
            self.scrubber.register_name_pair(value, default_value)
            return value
        else:
            return default_value


    def setUp(self):
        # Every test uses a different resource group name calculated from its
        # qualified test name.
        #
        # When running all tests serially, this allows us to delete
        # the resource group in teardown without waiting for the delete to
        # complete. The next test in line will use a different resource group,
        # so it won't have any trouble creating its resource group even if the
        # previous test resource group hasn't finished deleting.
        #
        # When running tests individually, if you try to run the same test
        # multiple times in a row, it's possible that the delete in the previous
        # teardown hasn't completed yet (because we don't wait), and that
        # would make resource group creation fail.
        # To avoid that, we also delete the resource group in the
        # setup, and we wait for that delete to complete.
        super(AzureTestCase, self).setUp()

    def tearDown(self):
        return super(AzureTestCase, self).tearDown()

    def create_basic_client(self, client_class, **kwargs):

        tenant_id = os.environ.get("AZURE_TENANT_ID", None)
        client_id = os.environ.get("AZURE_CLIENT_ID", None)
        secret = os.environ.get("AZURE_CLIENT_SECRET", None)

        if tenant_id and client_id and secret and self.is_live:
            if _is_autorest_v3(client_class):
                # Create azure-identity class
                from azure.identity import ClientSecretCredential
                credentials = ClientSecretCredential(
                    tenant_id=tenant_id,
                    client_id=client_id,
                    client_secret=secret
                )
            else:
                # Create msrestazure class
                from msrestazure.azure_active_directory import ServicePrincipalCredentials
                credentials = ServicePrincipalCredentials(
                    tenant=tenant_id,
                    client_id=client_id,
                    secret=secret
                )
        else:
            if _is_autorest_v3(client_class):
                credentials = self.settings.get_azure_core_credentials()
            else:
                credentials = self.settings.get_credentials()

        # Real client creation
        # FIXME decide what is the final argument for that
        # if self.is_playback():
        #     kwargs.setdefault("polling_interval", 0)
        if _is_autorest_v3(client_class):
            kwargs.setdefault("logging_enable", True)
            client = client_class(
                credential=credentials,
                **kwargs
            )
        else:
            client = client_class(
                credentials=credentials,
                **kwargs
            )

        if self.is_playback():
            try:
                client._config.polling_interval = 0  # FIXME in azure-mgmt-core, make this a kwargs
            except AttributeError:
                pass

        if hasattr(client, "config"):  # Autorest v2
            if self.is_playback():
                client.config.long_running_operation_timeout = 0
            client.config.enable_http_logger = True
        return client

    def create_random_name(self, name):
        return get_resource_name(name, self.qualified_test_name.encode())

    def get_resource_name(self, name):
        """Alias to create_random_name for back compatibility."""
        return self.create_random_name(name)

    def get_replayable_random_resource_name(self, name):
        """In a replay scenario, (is not live) gives the static moniker.  In the random scenario, gives generated name."""
        if self.is_live:
            created_name = self.create_random_name(name)
            self.scrubber.register_name_pair(
                created_name,
                name
            )
        return name

    def get_preparer_resource_name(self, prefix):
        """Random name generation for use by preparers.

        If prefix is a blank string, use the fully qualified test name instead.
        This is what legacy tests do for resource groups."""
        return self.get_resource_name(prefix or self.qualified_test_name.replace('.', '_'))

    @staticmethod
    def await_prepared_test(test_fn):
        """Synchronous wrapper for async test methods. Used to avoid making changes
        upstream to AbstractPreparer (which doesn't await the functions it wraps)
        """

        if sys.version_info < (3, 5):
            raise ImportError("Async wrapper is not needed for Python 2.7 code.")

        import asyncio
        @functools.wraps(test_fn)
        def run(test_class_instance, *args, **kwargs):
            trim_kwargs_from_test_function(test_fn, kwargs)
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(test_fn(test_class_instance, **kwargs))

        return run
