# coding=utf-8
# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

# pylint: disable=protected-access

from typing import (
    Any,
    IO,
    Union,
    List,
    TYPE_CHECKING
)
from azure.core.tracing.decorator import distributed_trace
from azure.core.polling.base_polling import LROBasePolling

from ._response_handlers import (
    prepare_prebuilt_models,
    prepare_content_result,
    prepare_form_result
)
from ._helpers import get_content_type
from ._form_base_client import FormRecognizerClientBase
from ._polling import AnalyzePolling
if TYPE_CHECKING:
    from azure.core.polling import LROPoller
    from ._models import FormPage, RecognizedForm


class FormRecognizerClient(FormRecognizerClientBase):
    """FormRecognizerClient extracts information from forms and images into structured data.
    It is the interface to use for analyzing receipts, recognizing content/layout from
    forms, and analyzing custom forms from trained models. It provides different methods
    based on inputs from a URL and inputs from a stream.

    :param str endpoint: Supported Cognitive Services endpoints (protocol and hostname,
        for example: https://westus2.api.cognitive.microsoft.com).
    :param credential: Credentials needed for the client to connect to Azure.
        This is an instance of AzureKeyCredential if using an API key or a token
        credential from :mod:`azure.identity`.
    :type credential: :class:`~azure.core.credentials.AzureKeyCredential` or
        :class:`~azure.core.credentials.TokenCredential`
    :keyword api_version:
        The API version of the service to use for requests. It defaults to the latest service version.
        Setting to an older version may result in reduced feature compatibility.
    :paramtype api_version: str or ~azure.ai.formrecognizer.FormRecognizerApiVersion

    .. admonition:: Example:

        .. literalinclude:: ../samples/sample_authentication.py
            :start-after: [START create_fr_client_with_key]
            :end-before: [END create_fr_client_with_key]
            :language: python
            :dedent: 8
            :caption: Creating the FormRecognizerClient with an endpoint and API key.

        .. literalinclude:: ../samples/sample_authentication.py
            :start-after: [START create_fr_client_with_aad]
            :end-before: [END create_fr_client_with_aad]
            :language: python
            :dedent: 8
            :caption: Creating the FormRecognizerClient with a token credential.
    """

    def _prebuilt_callback(self, raw_response, _, headers, **kwargs):  # pylint: disable=unused-argument
        analyze_result = self._deserialize(self._generated_models.AnalyzeOperationResult, raw_response)
        return prepare_prebuilt_models(analyze_result, **kwargs)

    @distributed_trace
    def begin_recognize_receipts(self, receipt, **kwargs):
        # type: (Union[bytes, IO[bytes]], Any) -> LROPoller[List[RecognizedForm]]
        """Extract field text and semantic values from a given sales receipt.
        The input document must be of one of the supported content types - 'application/pdf',
        'image/jpeg', 'image/png' or 'image/tiff'.

        See fields found on a receipt here:
        https://aka.ms/formrecognizer/receiptfields

        :param receipt: JPEG, PNG, PDF and TIFF type file stream or bytes.
        :type receipt: bytes or IO[bytes]
        :keyword bool include_field_elements:
            Whether or not to include field elements such as lines and words in addition to form fields.
        :keyword content_type: Media type of the body sent to the API. Content-type is
            auto-detected, but can be overridden by passing this keyword argument. For options,
            see :class:`~azure.ai.formrecognizer.FormContentType`.
        :paramtype content_type: str or ~azure.ai.formrecognizer.FormContentType
        :keyword int polling_interval: Waiting time between two polls for LRO operations
            if no Retry-After header is present. Defaults to 5 seconds.
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword str locale: Locale of the receipt. Supported locales include: en-US, en-AU, en-CA, en-GB,
            and en-IN.
        :return: An instance of an LROPoller. Call `result()` on the poller
            object to return a list[:class:`~azure.ai.formrecognizer.RecognizedForm`].
        :rtype: ~azure.core.polling.LROPoller[list[~azure.ai.formrecognizer.RecognizedForm]]
        :raises ~azure.core.exceptions.HttpResponseError:
        .. versionadded:: v2.1-preview
            The *locale* keyword argument

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_recognize_receipts.py
                :start-after: [START recognize_receipts]
                :end-before: [END recognize_receipts]
                :language: python
                :dedent: 8
                :caption: Recognize sales receipt fields.
        """
        locale = kwargs.pop("locale", None)
        content_type = kwargs.pop("content_type", None)
        include_field_elements = kwargs.pop("include_field_elements", False)
        if content_type == "application/json":
            raise TypeError("Call begin_recognize_receipts_from_url() to analyze a receipt from a URL.")
        cls = kwargs.pop("cls", self._prebuilt_callback)
        if content_type is None:
            content_type = get_content_type(receipt)

        # FIXME: part of this code will be removed once autorest can handle diff mixin
        # signatures across API versions
        if locale:
            if self.api_version == "2.1-preview.1":
                kwargs.update({"locale": locale})
            else:
                raise ValueError("'locale' is only available for API version V2_1_PREVIEW and up")

        return self._client.begin_analyze_receipt_async(  # type: ignore
            file_stream=receipt,
            content_type=content_type,
            include_text_details=include_field_elements,
            cls=cls,
            polling=True,
            **kwargs
        )

    @distributed_trace
    def begin_recognize_receipts_from_url(self, receipt_url, **kwargs):
        # type: (str, Any) -> LROPoller[List[RecognizedForm]]
        """Extract field text and semantic values from a given sales receipt.
        The input document must be the location (URL) of the receipt to be analyzed.

        See fields found on a receipt here:
        https://aka.ms/formrecognizer/receiptfields

        :param str receipt_url: The URL of the receipt to analyze. The input must be a valid, encoded URL
            of one of the supported formats: JPEG, PNG, PDF and TIFF.
        :keyword bool include_field_elements:
            Whether or not to include field elements such as lines and words in addition to form fields.
        :keyword int polling_interval: Waiting time between two polls for LRO operations
            if no Retry-After header is present. Defaults to 5 seconds.
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword str locale: Locale of the receipt. Supported locales include: en-US, en-AU, en-CA, en-GB,
            and en-IN.
        :return: An instance of an LROPoller. Call `result()` on the poller
            object to return a list[:class:`~azure.ai.formrecognizer.RecognizedForm`].
        :rtype: ~azure.core.polling.LROPoller[list[~azure.ai.formrecognizer.RecognizedForm]]
        :raises ~azure.core.exceptions.HttpResponseError:
        .. versionadded:: v2.1-preview
            The *locale* keyword argument

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_recognize_receipts_from_url.py
                :start-after: [START recognize_receipts_from_url]
                :end-before: [END recognize_receipts_from_url]
                :language: python
                :dedent: 8
                :caption: Recognize sales receipt fields from a URL.
        """
        locale = kwargs.pop("locale", None)
        include_field_elements = kwargs.pop("include_field_elements", False)
        cls = kwargs.pop("cls", self._prebuilt_callback)

        # FIXME: part of this code will be removed once autorest can handle diff mixin
        # signatures across API versions
        if locale:
            if self.api_version == "2.1-preview.1":
                kwargs.update({"locale": locale})
            else:
                raise ValueError("'locale' is only available for API version V2_1_PREVIEW and up")
        return self._client.begin_analyze_receipt_async(  # type: ignore
            file_stream={"source": receipt_url},
            include_text_details=include_field_elements,
            cls=cls,
            polling=True,
            **kwargs
        )

    @distributed_trace
    def begin_recognize_business_cards(
            self,
            business_card,
            **kwargs
    ):
        # type: (Union[bytes, IO[bytes]], Any) -> LROPoller[List[RecognizedForm]]
        """Extract field text and semantic values from a given business card.
        The input document must be of one of the supported content types - 'application/pdf',
        'image/jpeg', 'image/png' or 'image/tiff'.

        See fields found on a business card here:
        https://aka.ms/formrecognizer/businesscardfields

        :param business_card: JPEG, PNG, PDF and TIFF type file stream or bytes.
        :type business_card: bytes or IO[bytes]
        :keyword str locale: Locale of the business card. Supported locales include: en-US, en-AU, en-CA, en-GB,
            and en-IN.
        :keyword bool include_field_elements:
            Whether or not to include field elements such as lines and words in addition to form fields.
        :keyword content_type: Media type of the body sent to the API. Content-type is
            auto-detected, but can be overridden by passing this keyword argument. For options,
            see :class:`~azure.ai.formrecognizer.FormContentType`.
        :paramtype content_type: str or ~azure.ai.formrecognizer.FormContentType
        :keyword int polling_interval: Waiting time between two polls for LRO operations
            if no Retry-After header is present. Defaults to 5 seconds.
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :return: An instance of an LROPoller. Call `result()` on the poller
            object to return a list[:class:`~azure.ai.formrecognizer.RecognizedForm`].
        :rtype: ~azure.core.polling.LROPoller[list[~azure.ai.formrecognizer.RecognizedForm]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        content_type = kwargs.pop("content_type", None)
        if content_type == "application/json":
            raise TypeError("Call begin_recognize_business_cards_from_url() to analyze a business card from a URL.")

        include_field_elements = kwargs.pop("include_field_elements", False)

        if content_type is None:
            content_type = get_content_type(business_card)

        try:
            return self._client.begin_analyze_business_card_async(  # type: ignore
                file_stream=business_card,
                content_type=content_type,
                include_text_details=include_field_elements,
                cls=kwargs.pop("cls", lambda pipeline_response, _, response_headers: self._prebuilt_callback(
                    pipeline_response, _, response_headers, business_card=True
                )),
                polling=True,
                **kwargs
            )
        except ValueError as e:
            if "begin_analyze_business_card_async" in str(e):
                raise ValueError(
                    "Method 'begin_recognize_business_cards' is only available for API version V2_1_PREVIEW and up"
                )
            raise e

    @distributed_trace
    def begin_recognize_business_cards_from_url(
            self,
            business_card_url,
            **kwargs
    ):
        # type: (str, Any) -> LROPoller[List[RecognizedForm]]
        """Extract field text and semantic values from a given business card.
        The input document must be the location (URL) of the card to be analyzed.

        See fields found on a business card here:
        https://aka.ms/formrecognizer/businesscardfields

        :param str business_card_url: The URL of the business card to analyze. The input must be a valid, encoded URL
            of one of the supported formats: JPEG, PNG, PDF and TIFF.
        :keyword str locale: Locale of the business card. Supported locales include: en-US, en-AU, en-CA, en-GB,
            and en-IN.
        :keyword bool include_field_elements:
            Whether or not to include field elements such as lines and words in addition to form fields.
        :keyword int polling_interval: Waiting time between two polls for LRO operations
            if no Retry-After header is present. Defaults to 5 seconds.
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :return: An instance of an LROPoller. Call `result()` on the poller
            object to return a list[:class:`~azure.ai.formrecognizer.RecognizedForm`].
        :rtype: ~azure.core.polling.LROPoller[list[~azure.ai.formrecognizer.RecognizedForm]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        include_field_elements = kwargs.pop("include_field_elements", False)

        try:
            return self._client.begin_analyze_business_card_async(  # type: ignore
                file_stream={"source": business_card_url},
                include_text_details=include_field_elements,
                cls=kwargs.pop("cls", lambda pipeline_response, _, response_headers: self._prebuilt_callback(
                    pipeline_response, _, response_headers, business_card=True
                )),
                polling=True,
                **kwargs
            )
        except ValueError as e:
            if "begin_analyze_business_card_async" in str(e):
                raise ValueError(
                    "Method 'begin_recognize_business_cards_from_url' is "
                    "only available for API version V2_1_PREVIEW and up"
                )
            raise e

    def _content_callback(self, raw_response, _, headers):  # pylint: disable=unused-argument
        analyze_result = self._deserialize(self._generated_models.AnalyzeOperationResult, raw_response)
        return prepare_content_result(analyze_result)

    @distributed_trace
    def begin_recognize_content(self, form, **kwargs):
        # type: (Union[bytes, IO[bytes]], Any) -> LROPoller[List[FormPage]]
        """Extract text and content/layout information from a given document.
        The input document must be of one of the supported content types - 'application/pdf',
        'image/jpeg', 'image/png' or 'image/tiff'.

        :param form: JPEG, PNG, PDF and TIFF type file stream or bytes.
        :type form: bytes or IO[bytes]
        :keyword content_type: Media type of the body sent to the API. Content-type is
            auto-detected, but can be overridden by passing this keyword argument. For options,
            see :class:`~azure.ai.formrecognizer.FormContentType`.
        :paramtype content_type: str or ~azure.ai.formrecognizer.FormContentType
        :keyword int polling_interval: Waiting time between two polls for LRO operations
            if no Retry-After header is present. Defaults to 5 seconds.
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :return: An instance of an LROPoller. Call `result()` on the poller
            object to return a list[:class:`~azure.ai.formrecognizer.FormPage`].
        :rtype: ~azure.core.polling.LROPoller[list[~azure.ai.formrecognizer.FormPage]]
        :raises ~azure.core.exceptions.HttpResponseError:

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_recognize_content.py
                :start-after: [START recognize_content]
                :end-before: [END recognize_content]
                :language: python
                :dedent: 8
                :caption: Recognize text and content/layout information from a form.
        """
        content_type = kwargs.pop("content_type", None)
        if content_type == "application/json":
            raise TypeError("Call begin_recognize_content_from_url() to analyze a document from a URL.")

        if content_type is None:
            content_type = get_content_type(form)

        return self._client.begin_analyze_layout_async(  # type: ignore
            file_stream=form,
            content_type=content_type,
            cls=kwargs.pop("cls", self._content_callback),
            polling=True,
            **kwargs
        )

    @distributed_trace
    def begin_recognize_content_from_url(self, form_url, **kwargs):
        # type: (str, Any) -> LROPoller[List[FormPage]]
        """Extract text and layout information from a given document.
        The input document must be the location (URL) of the document to be analyzed.

        :param str form_url: The URL of the form to analyze. The input must be a valid, encoded URL
            of one of the supported formats: JPEG, PNG, PDF and TIFF.
        :keyword int polling_interval: Waiting time between two polls for LRO operations
            if no Retry-After header is present. Defaults to 5 seconds.
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :return: An instance of an LROPoller. Call `result()` on the poller
            object to return a list[:class:`~azure.ai.formrecognizer.FormPage`].
        :rtype: ~azure.core.polling.LROPoller[list[~azure.ai.formrecognizer.FormPage]]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        return self._client.begin_analyze_layout_async(  # type: ignore
            file_stream={"source": form_url},
            cls=kwargs.pop("cls", self._content_callback),
            polling=True,
            **kwargs
        )

    @distributed_trace
    def begin_recognize_custom_forms(self, model_id, form, **kwargs):
        # type: (str, Union[bytes, IO[bytes]], Any) -> LROPoller[List[RecognizedForm]]
        """Analyze a custom form with a model trained with or without labels. The form
        to analyze should be of the same type as the forms that were used to train the model.
        The input document must be of one of the supported content types - 'application/pdf',
        'image/jpeg', 'image/png' or 'image/tiff'.

        :param str model_id: Custom model identifier.
        :param form: JPEG, PNG, PDF and TIFF type file stream or bytes.
        :type form: bytes or IO[bytes]
        :keyword bool include_field_elements:
            Whether or not to include field elements such as lines and words in addition to form fields.
        :keyword content_type: Media type of the body sent to the API. Content-type is
            auto-detected, but can be overridden by passing this keyword argument. For options,
            see :class:`~azure.ai.formrecognizer.FormContentType`.
        :paramtype content_type: str or ~azure.ai.formrecognizer.FormContentType
        :keyword int polling_interval: Waiting time between two polls for LRO operations
            if no Retry-After header is present. Defaults to 5 seconds.
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :return: An instance of an LROPoller. Call `result()` on the poller
            object to return a list[:class:`~azure.ai.formrecognizer.RecognizedForm`].
        :rtype: ~azure.core.polling.LROPoller[list[~azure.ai.formrecognizer.RecognizedForm]
        :raises ~azure.core.exceptions.HttpResponseError:

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_recognize_custom_forms.py
                :start-after: [START recognize_custom_forms]
                :end-before: [END recognize_custom_forms]
                :language: python
                :dedent: 8
                :caption: Recognize fields and values from a custom form.
        """

        if not model_id:
            raise ValueError("model_id cannot be None or empty.")

        polling_interval = kwargs.pop("polling_interval", self._client._config.polling_interval)
        continuation_token = kwargs.pop("continuation_token", None)
        content_type = kwargs.pop("content_type", None)
        if content_type == "application/json":
            raise TypeError("Call begin_recognize_custom_forms_from_url() to analyze a document from a URL.")

        include_field_elements = kwargs.pop("include_field_elements", False)
        if content_type is None:
            content_type = get_content_type(form)

        def analyze_callback(raw_response, _, headers):  # pylint: disable=unused-argument
            analyze_result = self._deserialize(self._generated_models.AnalyzeOperationResult, raw_response)
            return prepare_form_result(analyze_result, model_id)

        return self._client.begin_analyze_with_custom_model(  # type: ignore
            file_stream=form,
            model_id=model_id,
            include_text_details=include_field_elements,
            content_type=content_type,
            cls=kwargs.pop("cls", analyze_callback),
            polling=LROBasePolling(timeout=polling_interval, lro_algorithms=[AnalyzePolling()], **kwargs),
            continuation_token=continuation_token,
            **kwargs
        )

    @distributed_trace
    def begin_recognize_custom_forms_from_url(self, model_id, form_url, **kwargs):
        # type: (str, str, Any) -> LROPoller[List[RecognizedForm]]
        """Analyze a custom form with a model trained with or without labels. The form
        to analyze should be of the same type as the forms that were used to train the model.
        The input document must be the location (URL) of the document to be analyzed.

        :param str model_id: Custom model identifier.
        :param str form_url: The URL of the form to analyze. The input must be a valid, encoded URL
            of one of the supported formats: JPEG, PNG, PDF and TIFF.
        :keyword bool include_field_elements:
            Whether or not to include field elements such as lines and words in addition to form fields.
        :keyword int polling_interval: Waiting time between two polls for LRO operations
            if no Retry-After header is present. Defaults to 5 seconds.
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :return: An instance of an LROPoller. Call `result()` on the poller
            object to return a list[:class:`~azure.ai.formrecognizer.RecognizedForm`].
        :rtype: ~azure.core.polling.LROPoller[list[~azure.ai.formrecognizer.RecognizedForm]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

        if not model_id:
            raise ValueError("model_id cannot be None or empty.")

        polling_interval = kwargs.pop("polling_interval", self._client._config.polling_interval)
        continuation_token = kwargs.pop("continuation_token", None)
        include_field_elements = kwargs.pop("include_field_elements", False)

        def analyze_callback(raw_response, _, headers):  # pylint: disable=unused-argument
            analyze_result = self._deserialize(self._generated_models.AnalyzeOperationResult, raw_response)
            return prepare_form_result(analyze_result, model_id)

        return self._client.begin_analyze_with_custom_model(  # type: ignore
            file_stream={"source": form_url},
            model_id=model_id,
            include_text_details=include_field_elements,
            cls=kwargs.pop("cls", analyze_callback),
            polling=LROBasePolling(timeout=polling_interval, lro_algorithms=[AnalyzePolling()], **kwargs),
            continuation_token=continuation_token,
            **kwargs
        )

    def close(self):
        # type: () -> None
        """Close the :class:`~azure.ai.formrecognizer.FormRecognizerClient` session.
        """
        return self._client.close()

    def __enter__(self):
        # type: () -> FormRecognizerClient
        self._client.__enter__()  # pylint:disable=no-member
        return self

    def __exit__(self, *args):
        # type: (*Any) -> None
        self._client.__exit__(*args)  # pylint:disable=no-member
