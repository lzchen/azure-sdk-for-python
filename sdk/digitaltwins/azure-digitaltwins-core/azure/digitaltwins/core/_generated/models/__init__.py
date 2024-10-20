# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import DigitalTwinModelsAddOptions
    from ._models_py3 import DigitalTwinModelsDeleteOptions
    from ._models_py3 import DigitalTwinModelsGetByIdOptions
    from ._models_py3 import DigitalTwinModelsListOptions
    from ._models_py3 import DigitalTwinModelsUpdateOptions
    from ._models_py3 import DigitalTwinsAddOptions
    from ._models_py3 import DigitalTwinsAddRelationshipOptions
    from ._models_py3 import DigitalTwinsDeleteOptions
    from ._models_py3 import DigitalTwinsDeleteRelationshipOptions
    from ._models_py3 import DigitalTwinsGetByIdOptions
    from ._models_py3 import DigitalTwinsGetComponentOptions
    from ._models_py3 import DigitalTwinsGetRelationshipByIdOptions
    from ._models_py3 import DigitalTwinsListIncomingRelationshipsOptions
    from ._models_py3 import DigitalTwinsListRelationshipsOptions
    from ._models_py3 import DigitalTwinsModelData
    from ._models_py3 import DigitalTwinsSendComponentTelemetryOptions
    from ._models_py3 import DigitalTwinsSendTelemetryOptions
    from ._models_py3 import DigitalTwinsUpdateComponentOptions
    from ._models_py3 import DigitalTwinsUpdateOptions
    from ._models_py3 import DigitalTwinsUpdateRelationshipOptions
    from ._models_py3 import Error
    from ._models_py3 import ErrorResponse
    from ._models_py3 import EventRoute
    from ._models_py3 import EventRouteCollection
    from ._models_py3 import EventRoutesAddOptions
    from ._models_py3 import EventRoutesDeleteOptions
    from ._models_py3 import EventRoutesGetByIdOptions
    from ._models_py3 import EventRoutesListOptions
    from ._models_py3 import IncomingRelationship
    from ._models_py3 import IncomingRelationshipCollection
    from ._models_py3 import InnerError
    from ._models_py3 import PagedDigitalTwinsModelDataCollection
    from ._models_py3 import QueryResult
    from ._models_py3 import QuerySpecification
    from ._models_py3 import QueryTwinsOptions
    from ._models_py3 import RelationshipCollection
except (SyntaxError, ImportError):
    from ._models import DigitalTwinModelsAddOptions  # type: ignore
    from ._models import DigitalTwinModelsDeleteOptions  # type: ignore
    from ._models import DigitalTwinModelsGetByIdOptions  # type: ignore
    from ._models import DigitalTwinModelsListOptions  # type: ignore
    from ._models import DigitalTwinModelsUpdateOptions  # type: ignore
    from ._models import DigitalTwinsAddOptions  # type: ignore
    from ._models import DigitalTwinsAddRelationshipOptions  # type: ignore
    from ._models import DigitalTwinsDeleteOptions  # type: ignore
    from ._models import DigitalTwinsDeleteRelationshipOptions  # type: ignore
    from ._models import DigitalTwinsGetByIdOptions  # type: ignore
    from ._models import DigitalTwinsGetComponentOptions  # type: ignore
    from ._models import DigitalTwinsGetRelationshipByIdOptions  # type: ignore
    from ._models import DigitalTwinsListIncomingRelationshipsOptions  # type: ignore
    from ._models import DigitalTwinsListRelationshipsOptions  # type: ignore
    from ._models import DigitalTwinsModelData  # type: ignore
    from ._models import DigitalTwinsSendComponentTelemetryOptions  # type: ignore
    from ._models import DigitalTwinsSendTelemetryOptions  # type: ignore
    from ._models import DigitalTwinsUpdateComponentOptions  # type: ignore
    from ._models import DigitalTwinsUpdateOptions  # type: ignore
    from ._models import DigitalTwinsUpdateRelationshipOptions  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import ErrorResponse  # type: ignore
    from ._models import EventRoute  # type: ignore
    from ._models import EventRouteCollection  # type: ignore
    from ._models import EventRoutesAddOptions  # type: ignore
    from ._models import EventRoutesDeleteOptions  # type: ignore
    from ._models import EventRoutesGetByIdOptions  # type: ignore
    from ._models import EventRoutesListOptions  # type: ignore
    from ._models import IncomingRelationship  # type: ignore
    from ._models import IncomingRelationshipCollection  # type: ignore
    from ._models import InnerError  # type: ignore
    from ._models import PagedDigitalTwinsModelDataCollection  # type: ignore
    from ._models import QueryResult  # type: ignore
    from ._models import QuerySpecification  # type: ignore
    from ._models import QueryTwinsOptions  # type: ignore
    from ._models import RelationshipCollection  # type: ignore

__all__ = [
    'DigitalTwinModelsAddOptions',
    'DigitalTwinModelsDeleteOptions',
    'DigitalTwinModelsGetByIdOptions',
    'DigitalTwinModelsListOptions',
    'DigitalTwinModelsUpdateOptions',
    'DigitalTwinsAddOptions',
    'DigitalTwinsAddRelationshipOptions',
    'DigitalTwinsDeleteOptions',
    'DigitalTwinsDeleteRelationshipOptions',
    'DigitalTwinsGetByIdOptions',
    'DigitalTwinsGetComponentOptions',
    'DigitalTwinsGetRelationshipByIdOptions',
    'DigitalTwinsListIncomingRelationshipsOptions',
    'DigitalTwinsListRelationshipsOptions',
    'DigitalTwinsModelData',
    'DigitalTwinsSendComponentTelemetryOptions',
    'DigitalTwinsSendTelemetryOptions',
    'DigitalTwinsUpdateComponentOptions',
    'DigitalTwinsUpdateOptions',
    'DigitalTwinsUpdateRelationshipOptions',
    'Error',
    'ErrorResponse',
    'EventRoute',
    'EventRouteCollection',
    'EventRoutesAddOptions',
    'EventRoutesDeleteOptions',
    'EventRoutesGetByIdOptions',
    'EventRoutesListOptions',
    'IncomingRelationship',
    'IncomingRelationshipCollection',
    'InnerError',
    'PagedDigitalTwinsModelDataCollection',
    'QueryResult',
    'QuerySpecification',
    'QueryTwinsOptions',
    'RelationshipCollection',
]
