# pylint: disable=too-many-lines,too-many-statements
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, List, Literal, Optional, Type, TypeVar, Union

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict

from ... import models as _models
from ...operations._service_operations import (
    build_get_properties_request,
    build_list_shares_segment_request,
    build_set_properties_request,
)

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ServiceOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.storage.fileshare.aio.AzureFileStorage`'s
        :attr:`service` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def set_properties(  # pylint: disable=inconsistent-return-statements
        self, storage_service_properties: _models.StorageServiceProperties, timeout: Optional[int] = None, **kwargs: Any
    ) -> None:
        # pylint: disable=line-too-long
        """Sets properties for a storage account's File service endpoint, including properties for Storage
        Analytics metrics and CORS (Cross-Origin Resource Sharing) rules.

        :param storage_service_properties: The StorageService properties. Required.
        :type storage_service_properties: ~azure.storage.fileshare.models.StorageServiceProperties
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {  # pylint: disable=unsubscriptable-object
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        restype: Literal["service"] = kwargs.pop("restype", _params.pop("restype", "service"))
        comp: Literal["properties"] = kwargs.pop("comp", _params.pop("comp", "properties"))
        content_type: str = kwargs.pop("content_type", _headers.pop("Content-Type", "application/xml"))
        cls: ClsType[None] = kwargs.pop("cls", None)

        _content = self._serialize.body(storage_service_properties, "StorageServiceProperties", is_xml=True)

        _request = build_set_properties_request(
            url=self._config.url,
            timeout=timeout,
            file_request_intent=self._config.file_request_intent,
            restype=restype,
            comp=comp,
            content_type=content_type,
            version=self._config.version,
            content=_content,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        if cls:
            return cls(pipeline_response, None, response_headers)  # type: ignore

    @distributed_trace_async
    async def get_properties(self, timeout: Optional[int] = None, **kwargs: Any) -> _models.StorageServiceProperties:
        # pylint: disable=line-too-long
        """Gets the properties of a storage account's File service, including properties for Storage
        Analytics metrics and CORS (Cross-Origin Resource Sharing) rules.

        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :return: StorageServiceProperties or the result of cls(response)
        :rtype: ~azure.storage.fileshare.models.StorageServiceProperties
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {  # pylint: disable=unsubscriptable-object
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        restype: Literal["service"] = kwargs.pop("restype", _params.pop("restype", "service"))
        comp: Literal["properties"] = kwargs.pop("comp", _params.pop("comp", "properties"))
        cls: ClsType[_models.StorageServiceProperties] = kwargs.pop("cls", None)

        _request = build_get_properties_request(
            url=self._config.url,
            timeout=timeout,
            file_request_intent=self._config.file_request_intent,
            restype=restype,
            comp=comp,
            version=self._config.version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        deserialized = self._deserialize("StorageServiceProperties", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore

    @distributed_trace_async
    async def list_shares_segment(
        self,
        prefix: Optional[str] = None,
        marker: Optional[str] = None,
        maxresults: Optional[int] = None,
        include: Optional[List[Union[str, _models.ListSharesIncludeType]]] = None,
        timeout: Optional[int] = None,
        **kwargs: Any
    ) -> _models.ListSharesResponse:
        # pylint: disable=line-too-long
        """The List Shares Segment operation returns a list of the shares and share snapshots under the
        specified account.

        :param prefix: Filters the results to return only entries whose name begins with the specified
         prefix. Default value is None.
        :type prefix: str
        :param marker: A string value that identifies the portion of the list to be returned with the
         next list operation. The operation returns a marker value within the response body if the list
         returned was not complete. The marker value may then be used in a subsequent call to request
         the next set of list items. The marker value is opaque to the client. Default value is None.
        :type marker: str
        :param maxresults: Specifies the maximum number of entries to return. If the request does not
         specify maxresults, or specifies a value greater than 5,000, the server will return up to 5,000
         items. Default value is None.
        :type maxresults: int
        :param include: Include this parameter to specify one or more datasets to include in the
         response. Default value is None.
        :type include: list[str or ~azure.storage.fileshare.models.ListSharesIncludeType]
        :param timeout: The timeout parameter is expressed in seconds. For more information, see
         :code:`<a
         href="https://docs.microsoft.com/en-us/rest/api/storageservices/Setting-Timeouts-for-File-Service-Operations?redirectedfrom=MSDN">Setting
         Timeouts for File Service Operations.</a>`. Default value is None.
        :type timeout: int
        :return: ListSharesResponse or the result of cls(response)
        :rtype: ~azure.storage.fileshare.models.ListSharesResponse
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map: MutableMapping[int, Type[HttpResponseError]] = {  # pylint: disable=unsubscriptable-object
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        comp: Literal["list"] = kwargs.pop("comp", _params.pop("comp", "list"))
        cls: ClsType[_models.ListSharesResponse] = kwargs.pop("cls", None)

        _request = build_list_shares_segment_request(
            url=self._config.url,
            prefix=prefix,
            marker=marker,
            maxresults=maxresults,
            include=include,
            timeout=timeout,
            file_request_intent=self._config.file_request_intent,
            comp=comp,
            version=self._config.version,
            headers=_headers,
            params=_params,
        )
        _request.url = self._client.format_url(_request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            _request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.StorageError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        response_headers = {}
        response_headers["x-ms-request-id"] = self._deserialize("str", response.headers.get("x-ms-request-id"))
        response_headers["x-ms-version"] = self._deserialize("str", response.headers.get("x-ms-version"))

        deserialized = self._deserialize("ListSharesResponse", pipeline_response.http_response)

        if cls:
            return cls(pipeline_response, deserialized, response_headers)  # type: ignore

        return deserialized  # type: ignore
