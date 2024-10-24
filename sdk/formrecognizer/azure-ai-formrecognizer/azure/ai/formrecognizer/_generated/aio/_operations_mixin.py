# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
from msrest import Serializer, Deserializer
from typing import Any, AsyncIterable, Callable, Dict, Generic, IO, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.polling.async_base_polling import AsyncLROBasePolling


class FormRecognizerClientOperationsMixin(object):

    async def begin_analyze_business_card_async(
        self,
        include_text_details: Optional[bool] = False,
        locale: Optional[str] = None,
        file_stream: Optional[Union[IO, "models.SourcePath"]] = None,
        **kwargs
    ) -> AsyncLROPoller[None]:
        """Analyze Business Card.

        Extract field text and semantic values from a given business card document. The input document
        must be of one of the supported content types - 'application/pdf', 'image/jpeg', 'image/png' or
        'image/tiff'. Alternatively, use 'application/json' type to specify the location (Uri) of the
        document to be analyzed.

        :param include_text_details: Include text lines and element references in the result.
        :type include_text_details: bool
        :param locale: Locale of the business card. Supported locales include: en-AU, en-CA, en-GB, en-
         IN, en-US(default).
        :type locale: str
        :param file_stream: .json, .pdf, .jpg, .png or .tiff type file stream.
        :type file_stream: IO or ~azure.ai.formrecognizer.models.SourcePath
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_analyze_business_card_async')
        if api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_analyze_business_card_async'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.begin_analyze_business_card_async(include_text_details, locale, file_stream, **kwargs)

    async def begin_analyze_layout_async(
        self,
        file_stream: Optional[Union[IO, "models.SourcePath"]] = None,
        **kwargs
    ) -> AsyncLROPoller[None]:
        """Analyze Layout.

        Extract text and layout information from a given document. The input document must be of one of
        the supported content types - 'application/pdf', 'image/jpeg', 'image/png' or 'image/tiff'.
        Alternatively, use 'application/json' type to specify the location (Uri or local path) of the
        document to be analyzed.

        :param file_stream: .json, .pdf, .jpg, .png or .tiff type file stream.
        :type file_stream: IO or ~azure.ai.formrecognizer.models.SourcePath
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_analyze_layout_async')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_analyze_layout_async'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.begin_analyze_layout_async(file_stream, **kwargs)

    async def begin_analyze_receipt_async(
        self,
        include_text_details: Optional[bool] = False,
        locale: Optional[str] = None,
        file_stream: Optional[Union[IO, "models.SourcePath"]] = None,
        **kwargs
    ) -> AsyncLROPoller[None]:
        """Analyze Receipt.

        Extract field text and semantic values from a given receipt document. The input document must
        be of one of the supported content types - 'application/pdf', 'image/jpeg', 'image/png' or
        'image/tiff'. Alternatively, use 'application/json' type to specify the location (Uri) of the
        document to be analyzed.

        :param include_text_details: Include text lines and element references in the result.
        :type include_text_details: bool
        :param locale: Locale of the receipt. Supported locales include: en-AU, en-CA, en-GB, en-IN,
         en-US(default).
        :type locale: str
        :param file_stream: .json, .pdf, .jpg, .png or .tiff type file stream.
        :type file_stream: IO or ~azure.ai.formrecognizer.models.SourcePath
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_analyze_receipt_async')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_analyze_receipt_async'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        # FIXME: this is handwritten
        if api_version == '2.0':
            return await mixin_instance.begin_analyze_receipt_async(include_text_details, file_stream, **kwargs)
        elif api_version == '2.1-preview.1':
            return await mixin_instance.begin_analyze_receipt_async(include_text_details, locale, file_stream, **kwargs)

    async def begin_analyze_with_custom_model(
        self,
        model_id: str,
        include_text_details: Optional[bool] = False,
        file_stream: Optional[Union[IO, "models.SourcePath"]] = None,
        **kwargs
    ) -> AsyncLROPoller[None]:
        """Analyze Form.

        Extract key-value pairs, tables, and semantic values from a given document. The input document
        must be of one of the supported content types - 'application/pdf', 'image/jpeg', 'image/png' or
        'image/tiff'. Alternatively, use 'application/json' type to specify the location (Uri or local
        path) of the document to be analyzed.

        :param model_id: Model identifier.
        :type model_id: str
        :param include_text_details: Include text lines and element references in the result.
        :type include_text_details: bool
        :param file_stream: .json, .pdf, .jpg, .png or .tiff type file stream.
        :type file_stream: IO or ~azure.ai.formrecognizer.models.SourcePath
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_analyze_with_custom_model')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_analyze_with_custom_model'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.begin_analyze_with_custom_model(model_id, include_text_details, file_stream, **kwargs)

    async def begin_compose_custom_models_async(
        self,
        compose_request: "models.ComposeRequest",
        **kwargs
    ) -> AsyncLROPoller[None]:
        """Compose trained with labels models into one composed model.

        Compose request would include list of models ids.
        It would validate what all models either trained with labels model or composed model.
        It would validate limit of models put together.

        :param compose_request: Compose models.
        :type compose_request: ~azure.ai.formrecognizer.models.ComposeRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_compose_custom_models_async')
        if api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_compose_custom_models_async'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.begin_compose_custom_models_async(compose_request, **kwargs)

    async def begin_copy_custom_model(
        self,
        model_id: str,
        copy_request: "models.CopyRequest",
        **kwargs
    ) -> AsyncLROPoller[None]:
        """Copy Custom Model.

        Copy custom model stored in this resource (the source) to user specified target Form Recognizer
        resource.

        :param model_id: Model identifier.
        :type model_id: str
        :param copy_request: Copy request parameters.
        :type copy_request: ~azure.ai.formrecognizer.models.CopyRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_copy_custom_model')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_copy_custom_model'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.begin_copy_custom_model(model_id, copy_request, **kwargs)

    async def begin_train_custom_model_async(
        self,
        train_request: "models.TrainRequest",
        **kwargs
    ) -> AsyncLROPoller[None]:
        """Train Custom Model.

        Create and train a custom model. The request must include a source parameter that is either an
        externally accessible Azure storage blob container Uri (preferably a Shared Access Signature
        Uri) or valid path to a data folder in a locally mounted drive. When local paths are specified,
        they must follow the Linux/Unix path format and be an absolute path rooted to the input mount
        configuration setting value e.g., if '{Mounts:Input}' configuration setting value is '/input'
        then a valid source path would be '/input/contosodataset'. All data to be trained is expected
        to be under the source folder or sub folders under it. Models are trained using documents that
        are of the following content type - 'application/pdf', 'image/jpeg', 'image/png', 'image/tiff'.
        Other type of content is ignored.

        :param train_request: Training request parameters.
        :type train_request: ~azure.ai.formrecognizer.models.TrainRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        api_version = self._get_api_version('begin_train_custom_model_async')
        if api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'begin_train_custom_model_async'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.begin_train_custom_model_async(train_request, **kwargs)

    async def delete_custom_model(
        self,
        model_id: str,
        **kwargs
    ) -> None:
        """Delete Custom Model.

        Mark model for deletion. Model artifacts will be permanently removed within a predetermined
        period.

        :param model_id: Model identifier.
        :type model_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('delete_custom_model')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'delete_custom_model'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.delete_custom_model(model_id, **kwargs)

    async def generate_model_copy_authorization(
        self,
        **kwargs
    ) -> "models.CopyAuthorizationResult":
        """Generate Copy Authorization.

        Generate authorization to copy a model into the target Form Recognizer resource.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CopyAuthorizationResult, or the result of cls(response)
        :rtype: ~azure.ai.formrecognizer.models.CopyAuthorizationResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('generate_model_copy_authorization')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'generate_model_copy_authorization'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.generate_model_copy_authorization(**kwargs)

    async def get_analyze_business_card_result(
        self,
        result_id: str,
        **kwargs
    ) -> "models.AnalyzeOperationResult":
        """Get Analyze Business Card Result.

        Track the progress and obtain the result of the analyze business card operation.

        :param result_id: Analyze operation result identifier.
        :type result_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeOperationResult, or the result of cls(response)
        :rtype: ~azure.ai.formrecognizer.models.AnalyzeOperationResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('get_analyze_business_card_result')
        if api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'get_analyze_business_card_result'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.get_analyze_business_card_result(result_id, **kwargs)

    async def get_analyze_form_result(
        self,
        model_id: str,
        result_id: str,
        **kwargs
    ) -> "models.AnalyzeOperationResult":
        """Get Analyze Form Result.

        Obtain current status and the result of the analyze form operation.

        :param model_id: Model identifier.
        :type model_id: str
        :param result_id: Analyze operation result identifier.
        :type result_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeOperationResult, or the result of cls(response)
        :rtype: ~azure.ai.formrecognizer.models.AnalyzeOperationResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('get_analyze_form_result')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'get_analyze_form_result'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.get_analyze_form_result(model_id, result_id, **kwargs)

    async def get_analyze_layout_result(
        self,
        result_id: str,
        **kwargs
    ) -> "models.AnalyzeOperationResult":
        """Get Analyze Layout Result.

        Track the progress and obtain the result of the analyze layout operation.

        :param result_id: Analyze operation result identifier.
        :type result_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeOperationResult, or the result of cls(response)
        :rtype: ~azure.ai.formrecognizer.models.AnalyzeOperationResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('get_analyze_layout_result')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'get_analyze_layout_result'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.get_analyze_layout_result(result_id, **kwargs)

    async def get_analyze_receipt_result(
        self,
        result_id: str,
        **kwargs
    ) -> "models.AnalyzeOperationResult":
        """Get Analyze Receipt Result.

        Track the progress and obtain the result of the analyze receipt operation.

        :param result_id: Analyze operation result identifier.
        :type result_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AnalyzeOperationResult, or the result of cls(response)
        :rtype: ~azure.ai.formrecognizer.models.AnalyzeOperationResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('get_analyze_receipt_result')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'get_analyze_receipt_result'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.get_analyze_receipt_result(result_id, **kwargs)

    async def get_custom_model(
        self,
        model_id: str,
        include_keys: Optional[bool] = False,
        **kwargs
    ) -> "models.Model":
        """Get Custom Model.

        Get detailed information about a custom model.

        :param model_id: Model identifier.
        :type model_id: str
        :param include_keys: Include list of extracted keys in model information.
        :type include_keys: bool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Model, or the result of cls(response)
        :rtype: ~azure.ai.formrecognizer.models.Model
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('get_custom_model')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'get_custom_model'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.get_custom_model(model_id, include_keys, **kwargs)

    async def get_custom_model_copy_result(
        self,
        model_id: str,
        result_id: str,
        **kwargs
    ) -> "models.CopyOperationResult":
        """Get Custom Model Copy Result.

        Obtain current status and the result of a custom model copy operation.

        :param model_id: Model identifier.
        :type model_id: str
        :param result_id: Copy operation result identifier.
        :type result_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CopyOperationResult, or the result of cls(response)
        :rtype: ~azure.ai.formrecognizer.models.CopyOperationResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('get_custom_model_copy_result')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'get_custom_model_copy_result'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.get_custom_model_copy_result(model_id, result_id, **kwargs)

    async def get_custom_models(
        self,
        **kwargs
    ) -> "models.Models":
        """Get Custom Models.

        Get information about all custom models.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Models, or the result of cls(response)
        :rtype: ~azure.ai.formrecognizer.models.Models
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('get_custom_models')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'get_custom_models'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.get_custom_models(**kwargs)

    def list_custom_models(
        self,
        **kwargs
    ) -> AsyncItemPaged["models.Models"]:
        """List Custom Models.

        Get information about all custom models.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either Models or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~azure.ai.formrecognizer.models.Models]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('list_custom_models')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        elif api_version == '2.1-preview.1':
            from ..v2_1_preview_1.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'list_custom_models'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return mixin_instance.list_custom_models(**kwargs)

    async def train_custom_model_async(
        self,
        train_request: "models.TrainRequest",
        **kwargs
    ) -> None:
        """Train Custom Model.

        Create and train a custom model. The request must include a source parameter that is either an
        externally accessible Azure storage blob container Uri (preferably a Shared Access Signature
        Uri) or valid path to a data folder in a locally mounted drive. When local paths are specified,
        they must follow the Linux/Unix path format and be an absolute path rooted to the input mount
        configuration setting value e.g., if '{Mounts:Input}' configuration setting value is '/input'
        then a valid source path would be '/input/contosodataset'. All data to be trained is expected
        to be under the source folder or sub folders under it. Models are trained using documents that
        are of the following content type - 'application/pdf', 'image/jpeg', 'image/png', 'image/tiff'.
        Other type of content is ignored.

        :param train_request: Training request parameters.
        :type train_request: ~azure.ai.formrecognizer.models.TrainRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = self._get_api_version('train_custom_model_async')
        if api_version == '2.0':
            from ..v2_0.aio.operations import FormRecognizerClientOperationsMixin as OperationClass
        else:
            raise ValueError("API version {} does not have operation 'train_custom_model_async'".format(api_version))
        mixin_instance = OperationClass()
        mixin_instance._client = self._client
        mixin_instance._config = self._config
        mixin_instance._serialize = Serializer(self._models_dict(api_version))
        mixin_instance._serialize.client_side_validation = False
        mixin_instance._deserialize = Deserializer(self._models_dict(api_version))
        return await mixin_instance.train_custom_model_async(train_request, **kwargs)
