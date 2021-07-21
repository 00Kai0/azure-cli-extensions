# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import NetworkManagementClientConfiguration
from .operations import NetworkManagersOperations
from .operations import NetworkManagerCommitsOperations
from .operations import NetworkManagerDeploymentStatusOperations
from .operations import EffectiveVirtualNetworksOperations
from .operations import ActiveConfigurationsOperations
from .operations import ConnectivityConfigurationsOperations
from .operations import EffectiveConfigurationsOperations
from .operations import NetworkGroupsOperations
from .operations import SecurityConfigurationsOperations
from .operations import AdminRulesOperations
from .operations import UserRulesOperations
from .. import models


class NetworkManagementClient(object):
    """Network Client.

    :ivar network_managers: NetworkManagersOperations operations
    :vartype network_managers: azure.mgmt.network.v2021_02_preview.aio.operations.NetworkManagersOperations
    :ivar network_manager_commits: NetworkManagerCommitsOperations operations
    :vartype network_manager_commits: azure.mgmt.network.v2021_02_preview.aio.operations.NetworkManagerCommitsOperations
    :ivar network_manager_deployment_status: NetworkManagerDeploymentStatusOperations operations
    :vartype network_manager_deployment_status: azure.mgmt.network.v2021_02_preview.aio.operations.NetworkManagerDeploymentStatusOperations
    :ivar effective_virtual_networks: EffectiveVirtualNetworksOperations operations
    :vartype effective_virtual_networks: azure.mgmt.network.v2021_02_preview.aio.operations.EffectiveVirtualNetworksOperations
    :ivar active_configurations: ActiveConfigurationsOperations operations
    :vartype active_configurations: azure.mgmt.network.v2021_02_preview.aio.operations.ActiveConfigurationsOperations
    :ivar connectivity_configurations: ConnectivityConfigurationsOperations operations
    :vartype connectivity_configurations: azure.mgmt.network.v2021_02_preview.aio.operations.ConnectivityConfigurationsOperations
    :ivar effective_configurations: EffectiveConfigurationsOperations operations
    :vartype effective_configurations: azure.mgmt.network.v2021_02_preview.aio.operations.EffectiveConfigurationsOperations
    :ivar network_groups: NetworkGroupsOperations operations
    :vartype network_groups: azure.mgmt.network.v2021_02_preview.aio.operations.NetworkGroupsOperations
    :ivar security_configurations: SecurityConfigurationsOperations operations
    :vartype security_configurations: azure.mgmt.network.v2021_02_preview.aio.operations.SecurityConfigurationsOperations
    :ivar admin_rules: AdminRulesOperations operations
    :vartype admin_rules: azure.mgmt.network.v2021_02_preview.aio.operations.AdminRulesOperations
    :ivar user_rules: UserRulesOperations operations
    :vartype user_rules: azure.mgmt.network.v2021_02_preview.aio.operations.UserRulesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = NetworkManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.network_managers = NetworkManagersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_manager_commits = NetworkManagerCommitsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_manager_deployment_status = NetworkManagerDeploymentStatusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.effective_virtual_networks = EffectiveVirtualNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.active_configurations = ActiveConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.connectivity_configurations = ConnectivityConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.effective_configurations = EffectiveConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.network_groups = NetworkGroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.security_configurations = SecurityConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.admin_rules = AdminRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.user_rules = UserRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "NetworkManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
