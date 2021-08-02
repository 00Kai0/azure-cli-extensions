# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class MicrosoftSerialConsoleClientOperationsMixin(object):

    def get_console_status(
        self,
        default="default",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Union["models.SerialConsoleStatus", "models.GetSerialConsoleSubscriptionNotFound"]
        """Get the disabled status for a subscription.

        Gets whether or not Serial Console is disabled for a given subscription.

        :param default: Default parameter. Leave the value as "default".
        :type default: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SerialConsoleStatus or GetSerialConsoleSubscriptionNotFound, or the result of cls(response)
        :rtype: ~microsoft_serial_console_client.models.SerialConsoleStatus or ~microsoft_serial_console_client.models.GetSerialConsoleSubscriptionNotFound
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Union["models.SerialConsoleStatus", "models.GetSerialConsoleSubscriptionNotFound"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01"
        accept = "application/json"

        # Construct URL
        url = self.get_console_status.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'default': self._serialize.url("default", default, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('SerialConsoleStatus', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_console_status.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default}'}  # type: ignore

    def disable_console(
        self,
        default="default",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Union["models.DisableSerialConsoleResult", "models.GetSerialConsoleSubscriptionNotFound"]
        """Disable Serial Console for a subscription.

        Disables the Serial Console service for all VMs and VM scale sets in the provided subscription.

        :param default: Default parameter. Leave the value as "default".
        :type default: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DisableSerialConsoleResult or GetSerialConsoleSubscriptionNotFound, or the result of cls(response)
        :rtype: ~microsoft_serial_console_client.models.DisableSerialConsoleResult or ~microsoft_serial_console_client.models.GetSerialConsoleSubscriptionNotFound
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Union["models.DisableSerialConsoleResult", "models.GetSerialConsoleSubscriptionNotFound"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01"
        accept = "application/json"
        content_type = "application/json"

        # Construct URL
        url = self.disable_console.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'default': self._serialize.url("default", default, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content-type", content_type, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('DisableSerialConsoleResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    disable_console.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default}/disableConsole'}  # type: ignore

    def enable_console(
        self,
        default="default",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Union["models.EnableSerialConsoleResult", "models.GetSerialConsoleSubscriptionNotFound"]
        """Enable Serial Console for a subscription.

        Enables the Serial Console service for all VMs and VM scale sets in the provided subscription.

        :param default: Default parameter. Leave the value as "default".
        :type default: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EnableSerialConsoleResult or GetSerialConsoleSubscriptionNotFound, or the result of cls(response)
        :rtype: ~microsoft_serial_console_client.models.EnableSerialConsoleResult or ~microsoft_serial_console_client.models.GetSerialConsoleSubscriptionNotFound
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Union["models.EnableSerialConsoleResult", "models.GetSerialConsoleSubscriptionNotFound"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2018-05-01"
        accept = "application/json"
        content_type = "application/json"

        # Construct URL
        url = self.enable_console.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'default': self._serialize.url("default", default, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Content-Type'] = self._serialize.header("content-type", content_type, 'str')

        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('EnableSerialConsoleResult', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    enable_console.metadata = {'url': '/subscriptions/{subscriptionId}/providers/Microsoft.SerialConsole/consoleServices/{default}/enableConsole'}  # type: ignore
