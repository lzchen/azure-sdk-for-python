# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum. Indicates the action type. "Internal" refers to actions that are for internal only APIs."""

    INTERNAL = "Internal"


class ApiPortalApiTryOutEnabledState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether the API try-out feature is enabled or disabled. When enabled, users can try
    out the API by sending requests and viewing responses in API portal. When disabled, users
    cannot try out the API.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ApiPortalProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the API portal."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class ApmProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the APM."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"
    CANCELED = "Canceled"


class ApplicationAcceleratorProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the application accelerator."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"
    CANCELED = "Canceled"


class ApplicationLiveViewProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the Application Live View."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"
    CANCELED = "Canceled"


class AppResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the App."""

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"


class BackendProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """How ingress should communicate with this app backend service."""

    GRPC = "GRPC"
    DEFAULT = "Default"


class BindingType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Buildpack Binding Type."""

    APPLICATION_INSIGHTS = "ApplicationInsights"
    APACHE_SKY_WALKING = "ApacheSkyWalking"
    APP_DYNAMICS = "AppDynamics"
    DYNATRACE = "Dynatrace"
    NEW_RELIC = "NewRelic"
    ELASTIC_APM = "ElasticAPM"


class BuilderProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Builder provision status."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class BuildpackBindingProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the Buildpack Binding."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class BuildProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the KPack build result."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class BuildResultProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the KPack build result."""

    QUEUING = "Queuing"
    BUILDING = "Building"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class BuildServiceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the KPack build service."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class CertificateResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Certificate."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class ConfigServerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the config server."""

    NOT_AVAILABLE = "NotAvailable"
    DELETED = "Deleted"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"


class ConfigurationServiceGeneration(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The generation of the Application Configuration Service."""

    GEN1 = "Gen1"
    GEN2 = "Gen2"


class ConfigurationServiceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the Application Configuration Service."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class ContainerRegistryProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the Container Registry."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"
    CANCELED = "Canceled"


class CreatedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that created the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class CustomDomainResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Domain."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class CustomizedAcceleratorProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the customized accelerator."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"
    CANCELED = "Canceled"


class CustomizedAcceleratorType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the customized accelerator."""

    ACCELERATOR = "Accelerator"
    FRAGMENT = "Fragment"


class CustomizedAcceleratorValidateResultState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the customized accelerator validation result."""

    VALID = "Valid"
    """Customized accelerator properties are valid."""
    INVALID = "Invalid"
    """Customized accelerator properties are invalid."""


class DeploymentResourceProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Deployment."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class DeploymentResourceStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Status of the Deployment."""

    STOPPED = "Stopped"
    RUNNING = "Running"


class DevToolPortalFeatureState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the plugin."""

    ENABLED = "Enabled"
    """Enable the plugin in Dev Tool Portal."""
    DISABLED = "Disabled"
    """Disable the plugin in Dev Tool Portal."""


class DevToolPortalProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the Dev Tool Portal."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"
    CANCELED = "Canceled"


class GatewayCertificateVerification(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Whether to enable certificate verification or not."""

    ENABLED = "Enabled"
    """Enable certificate verification in Spring Cloud Gateway."""
    DISABLED = "Disabled"
    """Disable certificate verification in Spring Cloud Gateway."""


class GatewayProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the Spring Cloud Gateway."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class GatewayRouteConfigProtocol(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Protocol of routed Azure Spring Apps applications."""

    HTTP = "HTTP"
    HTTPS = "HTTPS"


class GitImplementation(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Git libraries used to support various repository providers."""

    GO_GIT = "go-git"
    LIBGIT2 = "libgit2"


class HTTPSchemeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Scheme to use for connecting to the host. Defaults to HTTP.

    Possible enum values:


    * ``"HTTP"`` means that the scheme used will be http://
    * ``"HTTPS"`` means that the scheme used will be https://.
    """

    HTTP = "HTTP"
    HTTPS = "HTTPS"


class KeyVaultCertificateAutoSync(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates whether to automatically synchronize certificate from key vault or not."""

    DISABLED = "Disabled"
    ENABLED = "Enabled"


class KPackBuildStageProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of this build stage resource."""

    NOT_STARTED = "NotStarted"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class LastModifiedByType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of identity that last modified the resource."""

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class ManagedIdentityType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the managed identity."""

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class MonitoringSettingState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the Monitoring Setting."""

    NOT_AVAILABLE = "NotAvailable"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"


class PowerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Power state of the Service."""

    RUNNING = "Running"
    STOPPED = "Stopped"


class PredefinedAcceleratorProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the predefined accelerator."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"


class PredefinedAcceleratorState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the predefined accelerator."""

    ENABLED = "Enabled"
    """Enable the predefined accelerator."""
    DISABLED = "Disabled"
    """Disable the predefined accelerator."""


class ProbeActionType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the action to take to perform the health check."""

    HTTP_GET_ACTION = "HTTPGetAction"
    TCP_SOCKET_ACTION = "TCPSocketAction"
    EXEC_ACTION = "ExecAction"


class ProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Provisioning state of the Service."""

    CREATING = "Creating"
    UPDATING = "Updating"
    STARTING = "Starting"
    STOPPING = "Stopping"
    DELETING = "Deleting"
    DELETED = "Deleted"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    MOVING = "Moving"
    MOVED = "Moved"
    MOVE_FAILED = "MoveFailed"


class ResourceSkuRestrictionsReasonCode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the reason for restriction. Possible values include: 'QuotaId',
    'NotAvailableForSubscription'.
    """

    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"


class ResourceSkuRestrictionsType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets the type of restrictions. Possible values include: 'Location', 'Zone'."""

    LOCATION = "Location"
    ZONE = "Zone"


class ServiceRegistryProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """State of the Service Registry."""

    CREATING = "Creating"
    UPDATING = "Updating"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"


class SessionAffinity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the affinity, set this to Cookie to enable session affinity."""

    COOKIE = "Cookie"
    NONE = "None"


class SkuScaleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Gets or sets the type of the scale."""

    NONE = "None"
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"


class StorageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the storage."""

    STORAGE_ACCOUNT = "StorageAccount"


class SupportedRuntimePlatform(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The platform of this runtime version (possible values: "Java" or ".NET")."""

    JAVA = "Java"
    _NET_CORE = ".NET Core"


class SupportedRuntimeValue(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The raw value which could be passed to deployment CRUD operations."""

    JAVA8 = "Java_8"
    JAVA11 = "Java_11"
    JAVA17 = "Java_17"
    NET_CORE31 = "NetCore_31"


class TestKeyType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the test key."""

    PRIMARY = "Primary"
    SECONDARY = "Secondary"


class TrafficDirection(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The direction of required traffic."""

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"


class TriggeredBuildResultProvisioningState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The provisioning state of this build result."""

    QUEUING = "Queuing"
    BUILDING = "Building"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    DELETING = "Deleting"
    CANCELED = "Canceled"


class Type(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of the underlying resource to mount as a persistent disk."""

    AZURE_FILE_VOLUME = "AzureFileVolume"
