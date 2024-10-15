# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import datetime
import locale
from os import environ
from os.path import isdir
import platform
import threading
import time
import warnings
from typing import Any, Callable, Dict, Optional, Tuple
from urllib.parse import urlparse

from opentelemetry.semconv.attributes.service_attributes import SERVICE_NAME
from opentelemetry.semconv.trace import DbSystemValues, SpanAttributes
from opentelemetry.semconv.resource import ResourceAttributes
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.util import ns_to_iso_str
from opentelemetry.util.types import Attributes, AttributeValue

from azure.core.pipeline.policies import BearerTokenCredentialPolicy
from azure.monitor.opentelemetry.exporter._generated.models import ContextTagKeys, TelemetryItem
from azure.monitor.opentelemetry.exporter._version import VERSION as ext_version
from azure.monitor.opentelemetry.exporter._constants import (
    _AKS_ARM_NAMESPACE_ID,
    _APPLICATION_INSIGHTS_RESOURCE_SCOPE,
    _PYTHON_ENABLE_OPENTELEMETRY,
    _INSTRUMENTATIONS_BIT_MAP,
    _FUNCTIONS_WORKER_RUNTIME,
    _WEBSITE_SITE_NAME,
)

# pylint:disable=too-many-return-statements
def _get_default_port_db(db_system: str) -> int:
    if db_system == DbSystemValues.POSTGRESQL.value:
        return 5432
    if db_system == DbSystemValues.CASSANDRA.value:
        return 9042
    if db_system in (DbSystemValues.MARIADB.value, DbSystemValues.MYSQL.value):
        return 3306
    if db_system == DbSystemValues.MSSQL.value:
        return 1433
    # TODO: Add in memcached
    if db_system == "memcached":
        return 11211
    if db_system == DbSystemValues.DB2.value:
        return 50000
    if db_system == DbSystemValues.ORACLE.value:
        return 1521
    if db_system == DbSystemValues.H2.value:
        return 8082
    if db_system == DbSystemValues.DERBY.value:
        return 1527
    if db_system == DbSystemValues.REDIS.value:
        return 6379
    return 0


def _get_default_port_http(scheme: Optional[str]) -> int:
    if scheme == "http":
        return 80
    if scheme == "https":
        return 443
    return 0


def _is_sql_db(db_system: str) -> bool:
    return db_system in (
        DbSystemValues.DB2.value,
        DbSystemValues.DERBY.value,
        DbSystemValues.MARIADB.value,
        DbSystemValues.MSSQL.value,
        DbSystemValues.ORACLE.value,
        DbSystemValues.SQLITE.value,
        DbSystemValues.OTHER_SQL.value,
        # spell-checker:ignore HSQLDB
        DbSystemValues.HSQLDB.value,
        DbSystemValues.H2.value,
      )


def _get_azure_sdk_target_source(attributes: Attributes) -> Optional[str]:
    # Currently logic only works for ServiceBus and EventHub
    if attributes:
        peer_address = attributes.get("peer.address")
        destination = attributes.get("message_bus.destination")
        if peer_address and destination:
            return str(peer_address) + "/" + str(destination)
    return None


def _get_scheme_for_http_dependency(attributes: Attributes) -> Optional[str]:
    if attributes:
        scheme = attributes.get(SpanAttributes.HTTP_SCHEME)
        if scheme:
            return str(scheme)


def _get_url_for_http_dependency(scheme: Optional[str], attributes: Attributes) -> Optional[str]:
    url = None
    if attributes:
        if SpanAttributes.HTTP_URL in attributes:
            url = attributes[SpanAttributes.HTTP_URL]
        elif scheme and SpanAttributes.HTTP_TARGET in attributes:
            http_target = attributes[SpanAttributes.HTTP_TARGET]
            if SpanAttributes.HTTP_HOST in attributes:
                url = "{}://{}{}".format(
                    str(scheme),
                    attributes[SpanAttributes.HTTP_HOST],
                    http_target,
                )
            elif SpanAttributes.NET_PEER_PORT in attributes:
                peer_port = attributes[SpanAttributes.NET_PEER_PORT]
                if SpanAttributes.NET_PEER_NAME in attributes:
                    peer_name = attributes[SpanAttributes.NET_PEER_NAME]
                    url = "{}://{}:{}{}".format(
                        scheme,
                        peer_name,
                        peer_port,
                        http_target,
                    )
                elif SpanAttributes.NET_PEER_IP in attributes:
                    peer_ip = attributes[SpanAttributes.NET_PEER_IP]
                    url = "{}://{}:{}{}".format(
                        scheme,
                        peer_ip,
                        peer_port,
                        http_target,
                    )
    return str(url)


def _get_target_and_path_for_http_dependency(target: Optional[str], url: Optional[str], scheme: Optional[str], attributes: Attributes) -> Tuple[Optional[str], str]:
    target_from_url = None
    path = ""
    if attributes:
        if url:
            try:
                parse_url = urlparse(url)
                path = parse_url.path
                if not path:
                    path = "/"
                if parse_url.port and parse_url.port == _get_default_port_http(scheme):
                    target_from_url = parse_url.hostname
                else:
                    target_from_url = parse_url.netloc
            except Exception:  # pylint: disable=broad-except
                pass
        if SpanAttributes.PEER_SERVICE not in attributes:
            if SpanAttributes.HTTP_HOST in attributes:
                host = attributes[SpanAttributes.HTTP_HOST]
                try:
                    # urlparse insists on absolute URLs starting with "//"
                    # This logic assumes host does not include a "//"
                    host_name = urlparse("//" + str(host))
                    if host_name.port == _get_default_port_http(scheme):
                        target = host_name.hostname
                    else:
                        target = str(host)
                except Exception:  # pylint: disable=broad-except
                    pass
            elif target_from_url:
                target = target_from_url
    return (target, path)