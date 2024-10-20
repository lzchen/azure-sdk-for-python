# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class DefaultError(msrest.serialization.Model):
    """Error body contract.

    :param error: Details about the error.
    :type error: ~workload_monitor_api.models.DefaultErrorAutoGenerated
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'DefaultErrorAutoGenerated'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DefaultError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class DefaultErrorAutoGenerated(msrest.serialization.Model):
    """Details about the error.

    :param code: Service-defined error code. This code serves as a sub-status for the HTTP error
     code specified in the response.
    :type code: str
    :param message: Human-readable representation of the error.
    :type message: str
    :param details: Details of the error.
    :type details: list[~workload_monitor_api.models.ErrorDetails]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ErrorDetails]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(DefaultErrorAutoGenerated, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.details = kwargs.get('details', None)


class ErrorDetails(msrest.serialization.Model):
    """Error details of the error body contract.

    :param code: Property level error code.
    :type code: str
    :param message: Human-readable representation of property-level error.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetails, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class Resource(msrest.serialization.Model):
    """The resource model definition for the ARM proxy resource, 'microsoft.workloadmonitor/monitors'.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Arm ID of this monitor.
    :vartype id: str
    :ivar name: Url-encoded monitor name.
    :vartype name: str
    :ivar type: Type of ARM resource.
    :vartype type: str
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
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class Monitor(Resource):
    """Information about a monitor.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Arm ID of this monitor.
    :vartype id: str
    :ivar name: Url-encoded monitor name.
    :vartype name: str
    :ivar type: Type of ARM resource.
    :vartype type: str
    :param monitor_name: Human-readable name of this monitor.
    :type monitor_name: str
    :param monitor_type: Type of this monitor.
    :type monitor_type: str
    :param monitored_object: Dynamic monitored object of this monitor.
    :type monitored_object: str
    :param parent_monitor_name: Name of this monitor's parent.
    :type parent_monitor_name: str
    :ivar previous_monitor_state: Current health state of this monitor. Possible values include:
     "Healthy", "Critical", "Warning", "Unknown".
    :vartype previous_monitor_state: str or ~workload_monitor_api.models.HealthState
    :ivar current_monitor_state: Current health state of this monitor. Possible values include:
     "Healthy", "Critical", "Warning", "Unknown".
    :vartype current_monitor_state: str or ~workload_monitor_api.models.HealthState
    :param evaluation_timestamp: Timestamp that this monitor was last evaluated.
    :type evaluation_timestamp: str
    :param current_state_first_observed_timestamp: Timestamp of this monitor's last state change.
    :type current_state_first_observed_timestamp: str
    :param last_reported_timestamp: Timestamp of this monitor's last reported state.
    :type last_reported_timestamp: str
    :param evidence: Evidence of this monitor's last state change.
    :type evidence: object
    :param monitor_configuration: Configuration settings at the time of this monitor's last state
     change.
    :type monitor_configuration: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'previous_monitor_state': {'readonly': True},
        'current_monitor_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'monitor_name': {'key': 'properties.monitorName', 'type': 'str'},
        'monitor_type': {'key': 'properties.monitorType', 'type': 'str'},
        'monitored_object': {'key': 'properties.monitoredObject', 'type': 'str'},
        'parent_monitor_name': {'key': 'properties.parentMonitorName', 'type': 'str'},
        'previous_monitor_state': {'key': 'properties.previousMonitorState', 'type': 'str'},
        'current_monitor_state': {'key': 'properties.currentMonitorState', 'type': 'str'},
        'evaluation_timestamp': {'key': 'properties.evaluationTimestamp', 'type': 'str'},
        'current_state_first_observed_timestamp': {'key': 'properties.currentStateFirstObservedTimestamp', 'type': 'str'},
        'last_reported_timestamp': {'key': 'properties.lastReportedTimestamp', 'type': 'str'},
        'evidence': {'key': 'properties.evidence', 'type': 'object'},
        'monitor_configuration': {'key': 'properties.monitorConfiguration', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Monitor, self).__init__(**kwargs)
        self.monitor_name = kwargs.get('monitor_name', None)
        self.monitor_type = kwargs.get('monitor_type', None)
        self.monitored_object = kwargs.get('monitored_object', None)
        self.parent_monitor_name = kwargs.get('parent_monitor_name', None)
        self.previous_monitor_state = None
        self.current_monitor_state = None
        self.evaluation_timestamp = kwargs.get('evaluation_timestamp', None)
        self.current_state_first_observed_timestamp = kwargs.get('current_state_first_observed_timestamp', None)
        self.last_reported_timestamp = kwargs.get('last_reported_timestamp', None)
        self.evidence = kwargs.get('evidence', None)
        self.monitor_configuration = kwargs.get('monitor_configuration', None)


class MonitorList(msrest.serialization.Model):
    """Basic information about the current status of a monitor.

    :param value: Array of monitors.
    :type value: list[~workload_monitor_api.models.Monitor]
    :param next_link: Link to next page if list is too long.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Monitor]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MonitorList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class MonitorStateChange(Resource):
    """Information about a state transition of a monitor.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Arm ID of this monitor.
    :vartype id: str
    :ivar name: Url-encoded monitor name.
    :vartype name: str
    :ivar type: Type of ARM resource.
    :vartype type: str
    :param monitor_name: Human-readable name of this monitor.
    :type monitor_name: str
    :param monitor_type: Type of this monitor.
    :type monitor_type: str
    :param monitored_object: Dynamic monitored object of this monitor.
    :type monitored_object: str
    :param evaluation_timestamp: Timestamp of that this event ocurred.
    :type evaluation_timestamp: str
    :param current_state_first_observed_timestamp: Timestamp of that this health state first
     ocurred.
    :type current_state_first_observed_timestamp: str
    :ivar previous_monitor_state: Previous health state. Possible values include: "Healthy",
     "Critical", "Warning", "Unknown".
    :vartype previous_monitor_state: str or ~workload_monitor_api.models.HealthState
    :ivar current_monitor_state: New health state. Possible values include: "Healthy", "Critical",
     "Warning", "Unknown".
    :vartype current_monitor_state: str or ~workload_monitor_api.models.HealthState
    :param evidence: Evidence of this monitor's last state change.
    :type evidence: object
    :param monitor_configuration: Configuration settings at the time of this monitor's last state
     change.
    :type monitor_configuration: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'previous_monitor_state': {'readonly': True},
        'current_monitor_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'monitor_name': {'key': 'properties.monitorName', 'type': 'str'},
        'monitor_type': {'key': 'properties.monitorType', 'type': 'str'},
        'monitored_object': {'key': 'properties.monitoredObject', 'type': 'str'},
        'evaluation_timestamp': {'key': 'properties.evaluationTimestamp', 'type': 'str'},
        'current_state_first_observed_timestamp': {'key': 'properties.currentStateFirstObservedTimestamp', 'type': 'str'},
        'previous_monitor_state': {'key': 'properties.previousMonitorState', 'type': 'str'},
        'current_monitor_state': {'key': 'properties.currentMonitorState', 'type': 'str'},
        'evidence': {'key': 'properties.evidence', 'type': 'object'},
        'monitor_configuration': {'key': 'properties.monitorConfiguration', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MonitorStateChange, self).__init__(**kwargs)
        self.monitor_name = kwargs.get('monitor_name', None)
        self.monitor_type = kwargs.get('monitor_type', None)
        self.monitored_object = kwargs.get('monitored_object', None)
        self.evaluation_timestamp = kwargs.get('evaluation_timestamp', None)
        self.current_state_first_observed_timestamp = kwargs.get('current_state_first_observed_timestamp', None)
        self.previous_monitor_state = None
        self.current_monitor_state = None
        self.evidence = kwargs.get('evidence', None)
        self.monitor_configuration = kwargs.get('monitor_configuration', None)


class MonitorStateChangeList(msrest.serialization.Model):
    """The monitor history of a monitor.

    :param value: Array of state change transitions.
    :type value: list[~workload_monitor_api.models.MonitorStateChange]
    :param next_link: Link to next page if list is too long.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MonitorStateChange]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MonitorStateChangeList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class Operation(msrest.serialization.Model):
    """Operation supported by the resource provider.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Name of the operation.
    :type name: str
    :param display: Required. The properties of the resource operation.
    :type display: ~workload_monitor_api.models.OperationDisplay
    :param origin: Required. The origin of the operation.
    :type origin: str
    """

    _validation = {
        'name': {'required': True},
        'display': {'required': True},
        'origin': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.display = kwargs['display']
        self.origin = kwargs['origin']


class OperationDisplay(msrest.serialization.Model):
    """The properties of the resource operation.

    All required parameters must be populated in order to send to Azure.

    :param provider: Required. Provider name of this operation.
    :type provider: str
    :param resource: Required. Resource name of this operation.
    :type resource: str
    :param operation: Required. Operation name of the operation.
    :type operation: str
    :param description: Required. Description of the operation.
    :type description: str
    """

    _validation = {
        'provider': {'required': True},
        'resource': {'required': True},
        'operation': {'required': True},
        'description': {'required': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs['provider']
        self.resource = kwargs['resource']
        self.operation = kwargs['operation']
        self.description = kwargs['description']


class OperationList(msrest.serialization.Model):
    """List of possible operations.

    :param value: Array of possible operations.
    :type value: list[~workload_monitor_api.models.Operation]
    :param next_link: Link to next page if list is too long.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)
