# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._microsoft_datadog_client_enums import *


class DatadogApiKey(msrest.serialization.Model):
    """DatadogApiKey.

    All required parameters must be populated in order to send to Azure.

    :param created_by: The user that created the API key.
    :type created_by: str
    :param name: The name of the API key.
    :type name: str
    :param key: Required. The value of the API key.
    :type key: str
    :param created: The time of creation of the API key.
    :type created: str
    """

    _validation = {
        'key': {'required': True},
    }

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'key': {'key': 'key', 'type': 'str'},
        'created': {'key': 'created', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        key: str,
        created_by: Optional[str] = None,
        name: Optional[str] = None,
        created: Optional[str] = None,
        **kwargs
    ):
        super(DatadogApiKey, self).__init__(**kwargs)
        self.created_by = created_by
        self.name = name
        self.key = key
        self.created = created


class DatadogApiKeyListResponse(msrest.serialization.Model):
    """Response of a list operation.

    :param value: Results of a list operation.
    :type value: list[~microsoft_datadog_client.models.DatadogApiKey]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DatadogApiKey]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["DatadogApiKey"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(DatadogApiKeyListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class DatadogHost(msrest.serialization.Model):
    """DatadogHost.

    :param name: The name of the host.
    :type name: str
    :param aliases: The aliases for the host.
    :type aliases: list[str]
    :param apps: The Datadog integrations reporting metrics for the host.
    :type apps: list[str]
    :param meta:
    :type meta: ~microsoft_datadog_client.models.DatadogHostMetadata
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'aliases': {'key': 'aliases', 'type': '[str]'},
        'apps': {'key': 'apps', 'type': '[str]'},
        'meta': {'key': 'meta', 'type': 'DatadogHostMetadata'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        aliases: Optional[List[str]] = None,
        apps: Optional[List[str]] = None,
        meta: Optional["DatadogHostMetadata"] = None,
        **kwargs
    ):
        super(DatadogHost, self).__init__(**kwargs)
        self.name = name
        self.aliases = aliases
        self.apps = apps
        self.meta = meta


class DatadogHostListResponse(msrest.serialization.Model):
    """Response of a list operation.

    :param value: Results of a list operation.
    :type value: list[~microsoft_datadog_client.models.DatadogHost]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DatadogHost]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["DatadogHost"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(DatadogHostListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class DatadogHostMetadata(msrest.serialization.Model):
    """DatadogHostMetadata.

    :param agent_version: The agent version.
    :type agent_version: str
    :param install_method:
    :type install_method: ~microsoft_datadog_client.models.DatadogInstallMethod
    :param logs_agent:
    :type logs_agent: ~microsoft_datadog_client.models.DatadogLogsAgent
    """

    _attribute_map = {
        'agent_version': {'key': 'agentVersion', 'type': 'str'},
        'install_method': {'key': 'installMethod', 'type': 'DatadogInstallMethod'},
        'logs_agent': {'key': 'logsAgent', 'type': 'DatadogLogsAgent'},
    }

    def __init__(
        self,
        *,
        agent_version: Optional[str] = None,
        install_method: Optional["DatadogInstallMethod"] = None,
        logs_agent: Optional["DatadogLogsAgent"] = None,
        **kwargs
    ):
        super(DatadogHostMetadata, self).__init__(**kwargs)
        self.agent_version = agent_version
        self.install_method = install_method
        self.logs_agent = logs_agent


class DatadogInstallMethod(msrest.serialization.Model):
    """DatadogInstallMethod.

    :param tool: The tool.
    :type tool: str
    :param tool_version: The tool version.
    :type tool_version: str
    :param installer_version: The installer version.
    :type installer_version: str
    """

    _attribute_map = {
        'tool': {'key': 'tool', 'type': 'str'},
        'tool_version': {'key': 'toolVersion', 'type': 'str'},
        'installer_version': {'key': 'installerVersion', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        tool: Optional[str] = None,
        tool_version: Optional[str] = None,
        installer_version: Optional[str] = None,
        **kwargs
    ):
        super(DatadogInstallMethod, self).__init__(**kwargs)
        self.tool = tool
        self.tool_version = tool_version
        self.installer_version = installer_version


class DatadogLogsAgent(msrest.serialization.Model):
    """DatadogLogsAgent.

    :param transport: The transport.
    :type transport: str
    """

    _attribute_map = {
        'transport': {'key': 'transport', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        transport: Optional[str] = None,
        **kwargs
    ):
        super(DatadogLogsAgent, self).__init__(**kwargs)
        self.transport = transport


class DatadogMonitorResource(msrest.serialization.Model):
    """DatadogMonitorResource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: ARM id of the monitor resource.
    :vartype id: str
    :ivar name: Name of the monitor resource.
    :vartype name: str
    :ivar type: The type of the monitor resource.
    :vartype type: str
    :param sku:
    :type sku: ~microsoft_datadog_client.models.ResourceSku
    :param properties: Properties specific to the monitor resource.
    :type properties: ~microsoft_datadog_client.models.MonitorProperties
    :param identity:
    :type identity: ~microsoft_datadog_client.models.IdentityProperties
    :param tags: A set of tags. Dictionary of :code:`<string>`.
    :type tags: dict[str, str]
    :param location: Required.
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'ResourceSku'},
        'properties': {'key': 'properties', 'type': 'MonitorProperties'},
        'identity': {'key': 'identity', 'type': 'IdentityProperties'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        sku: Optional["ResourceSku"] = None,
        properties: Optional["MonitorProperties"] = None,
        identity: Optional["IdentityProperties"] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(DatadogMonitorResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.sku = sku
        self.properties = properties
        self.identity = identity
        self.tags = tags
        self.location = location


class DatadogMonitorResourceListResponse(msrest.serialization.Model):
    """Response of a list operation.

    :param value: Results of a list operation.
    :type value: list[~microsoft_datadog_client.models.DatadogMonitorResource]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DatadogMonitorResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["DatadogMonitorResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(DatadogMonitorResourceListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class DatadogMonitorResourceUpdateParameters(msrest.serialization.Model):
    """The parameters for a PATCH request to a monitor resource.

    :param properties: The set of properties that can be update in a PATCH request to a monitor
     resource.
    :type properties: ~microsoft_datadog_client.models.MonitorUpdateProperties
    :param tags: A set of tags. The new tags of the monitor resource.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'MonitorUpdateProperties'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        properties: Optional["MonitorUpdateProperties"] = None,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(DatadogMonitorResourceUpdateParameters, self).__init__(**kwargs)
        self.properties = properties
        self.tags = tags


class DatadogOrganizationProperties(msrest.serialization.Model):
    """DatadogOrganizationProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the Datadog organization.
    :vartype name: str
    :ivar id: Id of the Datadog organization.
    :vartype id: str
    :param linking_auth_code: The auth code used to linking to an existing datadog organization.
    :type linking_auth_code: str
    :param linking_client_id: The client_id from an existing in exchange for an auth token to link
     organization.
    :type linking_client_id: str
    :param enterprise_app_id: The Id of the Enterprise App used for Single sign on.
    :type enterprise_app_id: str
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'linking_auth_code': {'key': 'linkingAuthCode', 'type': 'str'},
        'linking_client_id': {'key': 'linkingClientId', 'type': 'str'},
        'enterprise_app_id': {'key': 'enterpriseAppId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        linking_auth_code: Optional[str] = None,
        linking_client_id: Optional[str] = None,
        enterprise_app_id: Optional[str] = None,
        **kwargs
    ):
        super(DatadogOrganizationProperties, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.linking_auth_code = linking_auth_code
        self.linking_client_id = linking_client_id
        self.enterprise_app_id = enterprise_app_id


class DatadogSetPasswordLink(msrest.serialization.Model):
    """DatadogSetPasswordLink.

    :param set_password_link:
    :type set_password_link: str
    """

    _attribute_map = {
        'set_password_link': {'key': 'setPasswordLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        set_password_link: Optional[str] = None,
        **kwargs
    ):
        super(DatadogSetPasswordLink, self).__init__(**kwargs)
        self.set_password_link = set_password_link


class DatadogSingleSignOnProperties(msrest.serialization.Model):
    """DatadogSingleSignOnProperties.

    :param single_sign_on_state: Various states of the SSO resource. Possible values include:
     "Initial", "Enable", "Disable", "Existing".
    :type single_sign_on_state: str or ~microsoft_datadog_client.models.SingleSignOnStates
    :param enterprise_app_id: The Id of the Enterprise App used for Single sign-on.
    :type enterprise_app_id: str
    :param single_sign_on_url: The login URL specific to this Datadog Organization.
    :type single_sign_on_url: str
    """

    _attribute_map = {
        'single_sign_on_state': {'key': 'singleSignOnState', 'type': 'str'},
        'enterprise_app_id': {'key': 'enterpriseAppId', 'type': 'str'},
        'single_sign_on_url': {'key': 'singleSignOnUrl', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        single_sign_on_state: Optional[Union[str, "SingleSignOnStates"]] = None,
        enterprise_app_id: Optional[str] = None,
        single_sign_on_url: Optional[str] = None,
        **kwargs
    ):
        super(DatadogSingleSignOnProperties, self).__init__(**kwargs)
        self.single_sign_on_state = single_sign_on_state
        self.enterprise_app_id = enterprise_app_id
        self.single_sign_on_url = single_sign_on_url


class DatadogSingleSignOnResource(msrest.serialization.Model):
    """DatadogSingleSignOnResource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: ARM id of the resource.
    :vartype id: str
    :ivar name: Name of the configuration.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param properties:
    :type properties: ~microsoft_datadog_client.models.DatadogSingleSignOnProperties
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'DatadogSingleSignOnProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["DatadogSingleSignOnProperties"] = None,
        **kwargs
    ):
        super(DatadogSingleSignOnResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.properties = properties


class DatadogSingleSignOnResourceListResponse(msrest.serialization.Model):
    """Response of a list operation.

    :param value: Results of a list operation.
    :type value: list[~microsoft_datadog_client.models.DatadogSingleSignOnResource]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[DatadogSingleSignOnResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["DatadogSingleSignOnResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(DatadogSingleSignOnResourceListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ErrorResponseBody(msrest.serialization.Model):
    """ErrorResponseBody.

    :param code:
    :type code: str
    :param message:
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~microsoft_datadog_client.models.ErrorResponseBody]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorResponseBody]'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        details: Optional[List["ErrorResponseBody"]] = None,
        **kwargs
    ):
        super(ErrorResponseBody, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class FilteringTag(msrest.serialization.Model):
    """The definition of a filtering tag. Filtering tags are used for capturing resources and include/exclude them from being monitored.

    :param name: The name (also known as the key) of the tag.
    :type name: str
    :param value: The value of the tag.
    :type value: str
    :param action: Valid actions for a filtering tag. Exclusion takes priority over inclusion.
     Possible values include: "Include", "Exclude".
    :type action: str or ~microsoft_datadog_client.models.TagAction
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'action': {'key': 'action', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        value: Optional[str] = None,
        action: Optional[Union[str, "TagAction"]] = None,
        **kwargs
    ):
        super(FilteringTag, self).__init__(**kwargs)
        self.name = name
        self.value = value
        self.action = action


class IdentityProperties(msrest.serialization.Model):
    """IdentityProperties.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The identity ID.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type:  Possible values include: "SystemAssigned", "UserAssigned".
    :type type: str or ~microsoft_datadog_client.models.ManagedIdentityTypes
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[Union[str, "ManagedIdentityTypes"]] = None,
        **kwargs
    ):
        super(IdentityProperties, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = type


class LinkedResource(msrest.serialization.Model):
    """The definition of a linked resource.

    :param id: The ARM id of the linked resource.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(LinkedResource, self).__init__(**kwargs)
        self.id = id


class LinkedResourceListResponse(msrest.serialization.Model):
    """Response of a list operation.

    :param value: Results of a list operation.
    :type value: list[~microsoft_datadog_client.models.LinkedResource]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[LinkedResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["LinkedResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(LinkedResourceListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class LogRules(msrest.serialization.Model):
    """Set of rules for sending logs for the Monitor resource.

    :param send_aad_logs: Flag specifying if AAD logs should be sent for the Monitor resource.
    :type send_aad_logs: bool
    :param send_subscription_logs: Flag specifying if Azure subscription logs should be sent for
     the Monitor resource.
    :type send_subscription_logs: bool
    :param send_resource_logs: Flag specifying if Azure resource logs should be sent for the
     Monitor resource.
    :type send_resource_logs: bool
    :param filtering_tags: List of filtering tags to be used for capturing logs. This only takes
     effect if SendResourceLogs flag is enabled. If empty, all resources will be captured. If only
     Exclude action is specified, the rules will apply to the list of all available resources. If
     Include actions are specified, the rules will only include resources with the associated tags.
    :type filtering_tags: list[~microsoft_datadog_client.models.FilteringTag]
    """

    _attribute_map = {
        'send_aad_logs': {'key': 'sendAadLogs', 'type': 'bool'},
        'send_subscription_logs': {'key': 'sendSubscriptionLogs', 'type': 'bool'},
        'send_resource_logs': {'key': 'sendResourceLogs', 'type': 'bool'},
        'filtering_tags': {'key': 'filteringTags', 'type': '[FilteringTag]'},
    }

    def __init__(
        self,
        *,
        send_aad_logs: Optional[bool] = None,
        send_subscription_logs: Optional[bool] = None,
        send_resource_logs: Optional[bool] = None,
        filtering_tags: Optional[List["FilteringTag"]] = None,
        **kwargs
    ):
        super(LogRules, self).__init__(**kwargs)
        self.send_aad_logs = send_aad_logs
        self.send_subscription_logs = send_subscription_logs
        self.send_resource_logs = send_resource_logs
        self.filtering_tags = filtering_tags


class MetricRules(msrest.serialization.Model):
    """Set of rules for sending metrics for the Monitor resource.

    :param filtering_tags: List of filtering tags to be used for capturing metrics. If empty, all
     resources will be captured. If only Exclude action is specified, the rules will apply to the
     list of all available resources. If Include actions are specified, the rules will only include
     resources with the associated tags.
    :type filtering_tags: list[~microsoft_datadog_client.models.FilteringTag]
    """

    _attribute_map = {
        'filtering_tags': {'key': 'filteringTags', 'type': '[FilteringTag]'},
    }

    def __init__(
        self,
        *,
        filtering_tags: Optional[List["FilteringTag"]] = None,
        **kwargs
    ):
        super(MetricRules, self).__init__(**kwargs)
        self.filtering_tags = filtering_tags


class MonitoredResource(msrest.serialization.Model):
    """The properties of a resource currently being monitored by the Datadog monitor resource.

    :param id: The ARM id of the resource.
    :type id: str
    :param sending_metrics: Flag indicating if resource is sending metrics to Datadog.
    :type sending_metrics: bool
    :param reason_for_metrics_status: Reason for why the resource is sending metrics (or why it is
     not sending).
    :type reason_for_metrics_status: str
    :param sending_logs: Flag indicating if resource is sending logs to Datadog.
    :type sending_logs: bool
    :param reason_for_logs_status: Reason for why the resource is sending logs (or why it is not
     sending).
    :type reason_for_logs_status: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'sending_metrics': {'key': 'sendingMetrics', 'type': 'bool'},
        'reason_for_metrics_status': {'key': 'reasonForMetricsStatus', 'type': 'str'},
        'sending_logs': {'key': 'sendingLogs', 'type': 'bool'},
        'reason_for_logs_status': {'key': 'reasonForLogsStatus', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        sending_metrics: Optional[bool] = None,
        reason_for_metrics_status: Optional[str] = None,
        sending_logs: Optional[bool] = None,
        reason_for_logs_status: Optional[str] = None,
        **kwargs
    ):
        super(MonitoredResource, self).__init__(**kwargs)
        self.id = id
        self.sending_metrics = sending_metrics
        self.reason_for_metrics_status = reason_for_metrics_status
        self.sending_logs = sending_logs
        self.reason_for_logs_status = reason_for_logs_status


class MonitoredResourceListResponse(msrest.serialization.Model):
    """Response of a list operation.

    :param value: Results of a list operation.
    :type value: list[~microsoft_datadog_client.models.MonitoredResource]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MonitoredResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MonitoredResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(MonitoredResourceListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class MonitoringTagRules(msrest.serialization.Model):
    """Capture logs and metrics of Azure resources based on ARM tags.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Name of the rule set.
    :vartype name: str
    :ivar id: The id of the rule set.
    :vartype id: str
    :ivar type: The type of the rule set.
    :vartype type: str
    :param properties: Definition of the properties for a TagRules resource.
    :type properties: ~microsoft_datadog_client.models.MonitoringTagRulesProperties
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'MonitoringTagRulesProperties'},
    }

    def __init__(
        self,
        *,
        properties: Optional["MonitoringTagRulesProperties"] = None,
        **kwargs
    ):
        super(MonitoringTagRules, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.type = None
        self.properties = properties


class MonitoringTagRulesListResponse(msrest.serialization.Model):
    """Response of a list operation.

    :param value: Results of a list operation.
    :type value: list[~microsoft_datadog_client.models.MonitoringTagRules]
    :param next_link: Link to the next set of results, if any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MonitoringTagRules]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["MonitoringTagRules"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(MonitoringTagRulesListResponse, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class MonitoringTagRulesProperties(msrest.serialization.Model):
    """Definition of the properties for a TagRules resource.

    :param log_rules: Set of rules for sending logs for the Monitor resource.
    :type log_rules: ~microsoft_datadog_client.models.LogRules
    :param metric_rules: Set of rules for sending metrics for the Monitor resource.
    :type metric_rules: ~microsoft_datadog_client.models.MetricRules
    """

    _attribute_map = {
        'log_rules': {'key': 'logRules', 'type': 'LogRules'},
        'metric_rules': {'key': 'metricRules', 'type': 'MetricRules'},
    }

    def __init__(
        self,
        *,
        log_rules: Optional["LogRules"] = None,
        metric_rules: Optional["MetricRules"] = None,
        **kwargs
    ):
        super(MonitoringTagRulesProperties, self).__init__(**kwargs)
        self.log_rules = log_rules
        self.metric_rules = metric_rules


class MonitorProperties(msrest.serialization.Model):
    """Properties specific to the monitor resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param provisioning_state:  Possible values include: "Accepted", "Creating", "Updating",
     "Deleting", "Succeeded", "Failed", "Canceled", "Deleted", "NotSpecified".
    :type provisioning_state: str or ~microsoft_datadog_client.models.ProvisioningState
    :param monitoring_status: Flag specifying if the resource monitoring is enabled or disabled.
     Possible values include: "Enabled", "Disabled".
    :type monitoring_status: str or ~microsoft_datadog_client.models.MonitoringStatus
    :param marketplace_subscription_status: Flag specifying the Marketplace Subscription Status of
     the resource. If payment is not made in time, the resource will go in Suspended state. Possible
     values include: "Active", "Suspended".
    :type marketplace_subscription_status: str or
     ~microsoft_datadog_client.models.MarketplaceSubscriptionStatus
    :param datadog_organization_properties:
    :type datadog_organization_properties:
     ~microsoft_datadog_client.models.DatadogOrganizationProperties
    :param user_info:
    :type user_info: ~microsoft_datadog_client.models.UserInfo
    :ivar liftr_resource_category:  Possible values include: "Unknown", "MonitorLogs".
    :vartype liftr_resource_category: str or
     ~microsoft_datadog_client.models.LiftrResourceCategories
    :ivar liftr_resource_preference: The priority of the resource.
    :vartype liftr_resource_preference: int
    """

    _validation = {
        'liftr_resource_category': {'readonly': True},
        'liftr_resource_preference': {'readonly': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'monitoring_status': {'key': 'monitoringStatus', 'type': 'str'},
        'marketplace_subscription_status': {'key': 'marketplaceSubscriptionStatus', 'type': 'str'},
        'datadog_organization_properties': {'key': 'datadogOrganizationProperties', 'type': 'DatadogOrganizationProperties'},
        'user_info': {'key': 'userInfo', 'type': 'UserInfo'},
        'liftr_resource_category': {'key': 'liftrResourceCategory', 'type': 'str'},
        'liftr_resource_preference': {'key': 'liftrResourcePreference', 'type': 'int'},
    }

    def __init__(
        self,
        *,
        provisioning_state: Optional[Union[str, "ProvisioningState"]] = None,
        monitoring_status: Optional[Union[str, "MonitoringStatus"]] = None,
        marketplace_subscription_status: Optional[Union[str, "MarketplaceSubscriptionStatus"]] = None,
        datadog_organization_properties: Optional["DatadogOrganizationProperties"] = None,
        user_info: Optional["UserInfo"] = None,
        **kwargs
    ):
        super(MonitorProperties, self).__init__(**kwargs)
        self.provisioning_state = provisioning_state
        self.monitoring_status = monitoring_status
        self.marketplace_subscription_status = marketplace_subscription_status
        self.datadog_organization_properties = datadog_organization_properties
        self.user_info = user_info
        self.liftr_resource_category = None
        self.liftr_resource_preference = None


class MonitorUpdateProperties(msrest.serialization.Model):
    """The set of properties that can be update in a PATCH request to a monitor resource.

    :param monitoring_status: Flag specifying if the resource monitoring is enabled or disabled.
     Possible values include: "Enabled", "Disabled".
    :type monitoring_status: str or ~microsoft_datadog_client.models.MonitoringStatus
    """

    _attribute_map = {
        'monitoring_status': {'key': 'monitoringStatus', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        monitoring_status: Optional[Union[str, "MonitoringStatus"]] = None,
        **kwargs
    ):
        super(MonitorUpdateProperties, self).__init__(**kwargs)
        self.monitoring_status = monitoring_status


class OperationDisplay(msrest.serialization.Model):
    """The object that represents the operation.

    :param provider: Service provider, i.e., Microsoft.Datadog.
    :type provider: str
    :param resource: Type on which the operation is performed, e.g., 'monitors'.
    :type resource: str
    :param operation: Operation type, e.g., read, write, delete, etc.
    :type operation: str
    :param description: Description of the operation, e.g., 'Write monitors'.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        provider: Optional[str] = None,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = provider
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationListResult(msrest.serialization.Model):
    """Result of GET request to list the Microsoft.Datadog operations.

    :param value: List of operations supported by the Microsoft.Datadog provider.
    :type value: list[~microsoft_datadog_client.models.OperationResult]
    :param next_link: URL to get the next set of operation list results if there are any.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationResult]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["OperationResult"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class OperationResult(msrest.serialization.Model):
    """A Microsoft.Datadog REST API operation.

    :param name: Operation name, i.e., {provider}/{resource}/{operation}.
    :type name: str
    :param display: The object that represents the operation.
    :type display: ~microsoft_datadog_client.models.OperationDisplay
    :param is_data_action: Indicates whether the operation is a data action.
    :type is_data_action: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDisplay"] = None,
        is_data_action: Optional[bool] = None,
        **kwargs
    ):
        super(OperationResult, self).__init__(**kwargs)
        self.name = name
        self.display = display
        self.is_data_action = is_data_action


class ResourceProviderDefaultErrorResponse(msrest.serialization.Model):
    """ResourceProviderDefaultErrorResponse.

    :param error:
    :type error: ~microsoft_datadog_client.models.ErrorResponseBody
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorResponseBody'},
    }

    def __init__(
        self,
        *,
        error: Optional["ErrorResponseBody"] = None,
        **kwargs
    ):
        super(ResourceProviderDefaultErrorResponse, self).__init__(**kwargs)
        self.error = error


class ResourceSku(msrest.serialization.Model):
    """ResourceSku.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the SKU.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        **kwargs
    ):
        super(ResourceSku, self).__init__(**kwargs)
        self.name = name


class UserInfo(msrest.serialization.Model):
    """UserInfo.

    :param name: Name of the user.
    :type name: str
    :param email_address: Email of the user used by Datadog for contacting them if needed.
    :type email_address: str
    :param phone_number: Phone number of the user used by Datadog for contacting them if needed.
    :type phone_number: str
    """

    _validation = {
        'name': {'max_length': 50, 'min_length': 0},
        'email_address': {'pattern': r'^[A-Za-z0-9._%+-]+@(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}$'},
        'phone_number': {'max_length': 40, 'min_length': 0},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'email_address': {'key': 'emailAddress', 'type': 'str'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        email_address: Optional[str] = None,
        phone_number: Optional[str] = None,
        **kwargs
    ):
        super(UserInfo, self).__init__(**kwargs)
        self.name = name
        self.email_address = email_address
        self.phone_number = phone_number
