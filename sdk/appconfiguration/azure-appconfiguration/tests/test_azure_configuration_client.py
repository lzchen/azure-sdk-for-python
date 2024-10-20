# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from azure.core import MatchConditions
from devtools_testutils import AzureMgmtTestCase
from azure.core.exceptions import (
    ResourceModifiedError,
    ResourceNotFoundError,
    ResourceExistsError,
    AzureError,
)
from azure.appconfiguration import (
    ResourceReadOnlyError,
    AzureAppConfigurationClient,
    ConfigurationSetting,
)
from consts import (
    KEY,
    LABEL,
    TEST_VALUE,
    TEST_CONTENT_TYPE,
    LABEL_RESERVED_CHARS,
    PAGE_SIZE,
    KEY_UUID,
)
import pytest
import datetime
import os
import logging
import re

class AppConfigurationClientTest(AzureMgmtTestCase):
    def __init__(self, method_name):
        super(AppConfigurationClientTest, self).__init__(method_name)
        self.vcr.match_on = ["path", "method", "query"]
        if self.is_playback():
            connection_str = "Endpoint=https://fake_app_config.azconfig-test.io;Id=0-l4-s0:h5htBaY5Z1LwFz50bIQv;Secret=bgyvBgwsQIw0s8myrqJJI3nLrj81M/kzSgSuP4BBoVg="
        else:
            connection_str = os.getenv('APP_CONFIG_CONNECTION')
        self.app_config_client = AzureAppConfigurationClient.from_connection_string(connection_str)

    def setUp(self):
        super(AppConfigurationClientTest, self).setUp()
        self.test_config_setting = self._add_for_test(
            ConfigurationSetting(
                key=KEY,
                label=LABEL,
                value=TEST_VALUE,
                content_type=TEST_CONTENT_TYPE,
                tags={"tag1": "tag1", "tag2": "tag2"},
            )
        )
        self.test_config_setting_no_label = self._add_for_test(
            ConfigurationSetting(
                key=KEY,
                label=None,
                value=TEST_VALUE,
                content_type=TEST_CONTENT_TYPE,
                tags={"tag1": "tag1", "tag2": "tag2"},
            )
        )
        self.to_delete = [self.test_config_setting, self.test_config_setting_no_label]

    def tearDown(self):
        super(AppConfigurationClientTest, self).tearDown()
        for item in self.to_delete:
            self.app_config_client.delete_configuration_setting(
                key=item.key, label=item.label
            )

    def _add_for_test(self, kv):
        exist = bool(
            list(
                self.app_config_client.list_configuration_settings(
                    key_filter=kv.key, label_filter=kv.label
                )
            )
        )
        if exist:
            self._delete_from_test(kv.key, kv.label)
        return self.app_config_client.add_configuration_setting(kv)

    def _delete_from_test(self, key, label):
        try:
            self.app_config_client.delete_configuration_setting(key=key, label=label)
        except AzureError:
            logging.debug(
                "Error occurred removing configuration setting %s %s during unit test"
                % (key, label)
            )

    # method: add_configuration_setting
    def test_add_configuration_setting(self):
        kv = ConfigurationSetting(
            key=KEY + "_ADD",
            label=LABEL,
            value=TEST_VALUE,
            content_type=TEST_CONTENT_TYPE,
            tags={"tag1": "tag1", "tag2": "tag2"},
        )
        created_kv = self.app_config_client.add_configuration_setting(kv)
        self.to_delete.append(created_kv)
        assert (
            created_kv.label == kv.label
            and kv.value == kv.value
            and created_kv.content_type == kv.content_type
            and created_kv.tags == kv.tags
        )
        assert (
            created_kv.etag is not None
            and created_kv.last_modified is not None
            and created_kv.read_only is False
        )

    def test_add_existing_configuration_setting(self):
        with pytest.raises(ResourceExistsError):
            self.app_config_client.add_configuration_setting(
                ConfigurationSetting(
                    key=self.test_config_setting.key,
                    lable=self.test_config_setting.label,
                )
            )

    # method: set_configuration_setting
    def test_set_existing_configuration_setting_label_etag(self):
        to_set_kv = self.test_config_setting
        to_set_kv.value = to_set_kv.value + "a"
        to_set_kv.tags = {"a": "b", "c": "d"}
        set_kv = self.app_config_client.set_configuration_setting(to_set_kv)
        assert (
            to_set_kv.key == set_kv.key
            and to_set_kv.label == to_set_kv.label
            and to_set_kv.value == set_kv.value
            and to_set_kv.content_type == set_kv.content_type
            and to_set_kv.tags == set_kv.tags
            and to_set_kv.etag != set_kv.etag
        )

    def test_set_existing_configuration_setting_label_wrong_etag(self):
        to_set_kv = self.test_config_setting
        to_set_kv.value = to_set_kv.value + "a"
        to_set_kv.tags = {"a": "b", "c": "d"}
        to_set_kv.etag = "wrong etag"
        with pytest.raises(ResourceModifiedError):
            self.app_config_client.set_configuration_setting(to_set_kv, match_condition=MatchConditions.IfNotModified)

    def test_set_configuration_setting_etag(self):
        kv = ConfigurationSetting(
            key=KEY + "_SET",
            label=LABEL,
            value=TEST_VALUE,
            content_type=TEST_CONTENT_TYPE,
            tags={"tag1": "tag1", "tag2": "tag2"},
        )
        kv.etag = "random etag"
        with pytest.raises(ResourceModifiedError):
            self.app_config_client.set_configuration_setting(kv, match_condition=MatchConditions.IfNotModified)

    def test_set_configuration_setting_no_etag(self):
        to_set_kv = ConfigurationSetting(
            key=KEY + "_SET",
            label=LABEL,
            value=TEST_VALUE,
            content_type=TEST_CONTENT_TYPE,
            tags={"tag1": "tag1", "tag2": "tag2"},
        )
        set_kv = self.app_config_client.set_configuration_setting(to_set_kv)
        self.to_delete.append(to_set_kv)
        assert (
            to_set_kv.key == set_kv.key
            and to_set_kv.label == set_kv.label
            and to_set_kv.value == set_kv.value
            and to_set_kv.content_type == set_kv.content_type
            and to_set_kv.tags == set_kv.tags
            and to_set_kv.etag != set_kv.etag
        )

    # method: get_configuration_setting
    def test_get_configuration_setting_no_label(self):
        compare_kv = self.test_config_setting_no_label
        fetched_kv = self.app_config_client.get_configuration_setting(compare_kv.key)
        assert (
            fetched_kv.key == compare_kv.key
            and fetched_kv.value == compare_kv.value
            and fetched_kv.content_type == compare_kv.content_type
            and fetched_kv.tags == compare_kv.tags
        )
        assert fetched_kv.label is None

    def test_get_configuration_setting_label(self):
        compare_kv = self.test_config_setting
        fetched_kv = self.app_config_client.get_configuration_setting(
            compare_kv.key, compare_kv.label
        )
        assert (
            fetched_kv.key == compare_kv.key
            and fetched_kv.value == compare_kv.value
            and fetched_kv.content_type == compare_kv.content_type
            and fetched_kv.tags == compare_kv.tags
        )
        assert fetched_kv.label is not None

    def test_get_non_existing_configuration_setting(self):
        compare_kv = self.test_config_setting
        with pytest.raises(ResourceNotFoundError):
            self.app_config_client.get_configuration_setting(
                compare_kv.key, compare_kv.label + "a"
            )

    # method: delete_configuration_setting
    def test_delete_with_key_no_label(self):
        to_delete_kv = self.test_config_setting_no_label
        self.app_config_client.delete_configuration_setting(to_delete_kv.key)
        self.to_delete.remove(to_delete_kv)
        with pytest.raises(ResourceNotFoundError):
            self.app_config_client.get_configuration_setting(to_delete_kv.key)

    def test_delete_with_key_label(self):
        to_delete_kv = self.test_config_setting
        self.app_config_client.delete_configuration_setting(
            to_delete_kv.key, label=to_delete_kv.label
        )
        self.to_delete.remove(to_delete_kv)
        with pytest.raises(ResourceNotFoundError):
            self.app_config_client.get_configuration_setting(
                to_delete_kv.key, label=to_delete_kv.label
            )

    def test_delete_non_existing(self):
        deleted_kv = self.app_config_client.delete_configuration_setting(
            "not_exist_" + KEY
        )
        assert deleted_kv is None

    def test_delete_correct_etag(self):
        to_delete_kv = self.test_config_setting_no_label
        deleted_kv = self.app_config_client.delete_configuration_setting(
            to_delete_kv.key, etag=to_delete_kv.etag
        )
        self.to_delete.remove(to_delete_kv)
        assert deleted_kv is not None
        with pytest.raises(ResourceNotFoundError):
            self.app_config_client.get_configuration_setting(to_delete_kv.key)

    def test_delete_wrong_etag(self):
        to_delete_kv = self.test_config_setting_no_label
        with pytest.raises(ResourceModifiedError):
            self.app_config_client.delete_configuration_setting(
                to_delete_kv.key, etag="wrong etag", match_condition=MatchConditions.IfNotModified
            )

    # method: list_configuration_settings
    def test_list_configuration_settings_key_label(self):
        items = list(self.app_config_client.list_configuration_settings(
            label_filter=LABEL, key_filter=KEY
        ))
        assert len(items) == 1
        assert all(x.label == LABEL and x.label == LABEL for x in items)

    def test_list_configuration_settings_only_label(self):
        items = list(self.app_config_client.list_configuration_settings(label_filter=LABEL))
        assert len(items) == 1
        assert all(x.label == LABEL for x in items)

    def test_list_configuration_settings_only_key(self):
        items = list(self.app_config_client.list_configuration_settings(key_filter=KEY))
        assert len(items) == 2
        assert all(x.key == KEY for x in items)

    def test_list_configuration_settings_fields(self):
        items = list(self.app_config_client.list_configuration_settings(
            key_filter="*", label_filter=LABEL, fields=["key", "content_type"]
        ))
        assert len(items) == 1
        assert all(x.key and not x.label and x.content_type for x in items)

    def test_list_configuration_settings_reserved_chars(self):
        resered_char_kv = ConfigurationSetting(
            key=KEY, label=LABEL_RESERVED_CHARS, value=TEST_VALUE
        )
        resered_char_kv = self.app_config_client.add_configuration_setting(
            resered_char_kv
        )
        self.to_delete.append(resered_char_kv)
        escaped_label = re.sub(r"((?!^)\*(?!$)|\\|,)", r"\\\1", LABEL_RESERVED_CHARS)
        items = list(self.app_config_client.list_configuration_settings(
            label_filter=escaped_label
        ))
        assert len(items) == 1
        assert all(x.label == LABEL_RESERVED_CHARS for x in items)

    def test_list_configuration_settings_contains(self):
        items = list(self.app_config_client.list_configuration_settings(
            label_filter="*" + LABEL + "*"
        ))
        assert len(items) == 1
        assert all(x.label == LABEL for x in items)

    def test_list_configuration_settings_correct_etag(self):
        to_list_kv = self.test_config_setting
        custom_headers = {"If-Match": to_list_kv.etag}
        items = list(self.app_config_client.list_configuration_settings(
            key_filter=to_list_kv.key, label_filter=to_list_kv.label, headers=custom_headers
        ))
        assert len(items) == 1
        assert all(x.key == to_list_kv.key and x.label == to_list_kv.label for x in items)

    def test_list_configuration_settings_multi_pages(self):
        # create PAGE_SIZE+1 configuration settings to have at least two pages
        try:
            delete_me = [
                self.app_config_client.add_configuration_setting(
                    ConfigurationSetting(
                        key="multi_" + str(i) + KEY_UUID,
                        label="multi_label_" + str(i),
                        value="multi value",
                    )
                )
                for i in range(PAGE_SIZE + 1)
            ]
        except ResourceExistsError:
            pass
        items = self.app_config_client.list_configuration_settings(key_filter="multi_*")
        assert len(list(items)) > PAGE_SIZE

        # Remove the configuration settings
        try:
            [
                self.app_config_client.delete_configuration_setting(
                    key="multi_" + str(i) + KEY_UUID, label="multi_label_" + str(i)
                )
                for i in range(PAGE_SIZE + 1)
            ]
        except AzureError:
            pass

    def test_list_configuration_settings_null_label(self):
        items = self.app_config_client.list_configuration_settings(label_filter="\0")
        assert len(list(items)) > 0

    def test_list_configuration_settings_only_accepttime(self):
        exclude_today = self.app_config_client.list_configuration_settings(
            accept_datetime=datetime.datetime.today() + datetime.timedelta(days=-1)
        )
        all_inclusive = self.app_config_client.list_configuration_settings()
        assert len(list(all_inclusive)) > len(list(exclude_today))

    # method: list_revisions
    def test_list_revisions_key_label(self):
        to_list1 = self.test_config_setting
        items = list(self.app_config_client.list_revisions(
            label_filter=to_list1.label, key_filter=to_list1.key
        ))
        assert len(items) >= 2
        assert all(x.key == to_list1.key and x.label == to_list1.label for x in items)

    def test_list_revisions_only_label(self):
        items = list(self.app_config_client.list_revisions(label_filter=LABEL))
        assert len(items) >= 1
        assert all(x.label == LABEL for x in items)

    def test_list_revisions_key_no_label(self):
        items = list(self.app_config_client.list_revisions(key_filter=KEY))
        assert len(items) >= 1
        assert all(x.key == KEY for x in items)

    def test_list_revisions_fields(self):
        items = list(self.app_config_client.list_revisions(
            key_filter="*", label_filter=LABEL, fields=["key", "content_type"]
        ))
        assert all(x.key and not x.label and x.content_type and not x.tags and not x.etag for x in items)

    def test_list_revisions_correct_etag(self):
        to_list_kv = self.test_config_setting
        custom_headers = {"If-Match": to_list_kv.etag}
        items = list(self.app_config_client.list_revisions(
            key_filter=to_list_kv.key, label_filter=to_list_kv.label, headers=custom_headers
        ))
        assert len(items) >= 1
        assert all(x.key == to_list_kv.key and x.label == to_list_kv.label for x in items)

    def test_read_only(self):
        kv = self.test_config_setting_no_label
        read_only_kv = self.app_config_client.set_read_only(kv)
        assert read_only_kv.read_only
        readable_kv = self.app_config_client.set_read_only(read_only_kv, False)
        assert not readable_kv.read_only

    def test_delete_read_only(self):
        to_delete_kv = self.test_config_setting_no_label
        read_only_kv = self.app_config_client.set_read_only(to_delete_kv)
        with pytest.raises(ResourceReadOnlyError):
            self.app_config_client.delete_configuration_setting(to_delete_kv.key)
        self.app_config_client.set_read_only(read_only_kv, False)
        self.app_config_client.delete_configuration_setting(to_delete_kv.key)
        self.to_delete.remove(to_delete_kv)
        with pytest.raises(ResourceNotFoundError):
            self.app_config_client.get_configuration_setting(to_delete_kv.key)

    def test_set_read_only(self):
        to_set_kv = self.test_config_setting
        to_set_kv.value = to_set_kv.value + "a"
        to_set_kv.tags = {"a": "b", "c": "d"}
        read_only_kv = self.app_config_client.set_read_only(to_set_kv)
        with pytest.raises(ResourceReadOnlyError):
            self.app_config_client.set_configuration_setting(read_only_kv)
        readable_kv = self.app_config_client.set_read_only(read_only_kv, False)
        readable_kv.value = to_set_kv.value
        readable_kv.tags = to_set_kv.tags
        set_kv = self.app_config_client.set_configuration_setting(readable_kv)
        assert (
                to_set_kv.key == set_kv.key
                and to_set_kv.label == to_set_kv.label
                and to_set_kv.value == set_kv.value
                and to_set_kv.content_type == set_kv.content_type
                and to_set_kv.tags == set_kv.tags
                and to_set_kv.etag != set_kv.etag
        )
        set_kv.etag = "bad"
        with pytest.raises(ResourceModifiedError):
            self.app_config_client.set_read_only(set_kv, True, match_condition=MatchConditions.IfNotModified)
