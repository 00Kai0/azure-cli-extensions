# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ActiveConfiguration
    from ._models_py3 import ActiveConfigurationListResult
    from ._models_py3 import AddressPrefixItem
    from ._models_py3 import AdminRule
    from ._models_py3 import AdminRuleListResult
    from ._models_py3 import AzureAsyncOperationResult
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import Components1Jq1T4ISchemasManagedserviceidentityPropertiesUserassignedidentitiesAdditionalproperties
    from ._models_py3 import ConnectivityConfiguration
    from ._models_py3 import ConnectivityConfigurationListResult
    from ._models_py3 import ConnectivityGroupItem
    from ._models_py3 import EffectiveConfiguration
    from ._models_py3 import EffectiveVirtualNetwork
    from ._models_py3 import EffectiveVirtualNetworksListResult
    from ._models_py3 import EffectiveVirtualNetworksParameter
    from ._models_py3 import Error
    from ._models_py3 import ErrorDetails
    from ._models_py3 import ExtendedLocation
    from ._models_py3 import FailedImport
    from ._models_py3 import GroupMembersItem
    from ._models_py3 import ManagedServiceIdentity
    from ._models_py3 import NetworkGroup
    from ._models_py3 import NetworkGroupListResult
    from ._models_py3 import NetworkManager
    from ._models_py3 import NetworkManagerCommit
    from ._models_py3 import NetworkManagerDeploymentStatus
    from ._models_py3 import NetworkManagerDeploymentStatusListResult
    from ._models_py3 import NetworkManagerDeploymentStatusParameter
    from ._models_py3 import NetworkManagerEffectiveConfigurationListResult
    from ._models_py3 import NetworkManagerListResult
    from ._models_py3 import NetworkManagerPropertiesNetworkManagerScopes
    from ._models_py3 import NetworkManagerSecurityConfigurationImport
    from ._models_py3 import NetworkManagerSecurityGroupItem
    from ._models_py3 import NetworkSecurityGroupImport
    from ._models_py3 import ProxyResource
    from ._models_py3 import Resource
    from ._models_py3 import SecurityConfiguration
    from ._models_py3 import SecurityConfigurationImportResult
    from ._models_py3 import SecurityConfigurationListResult
    from ._models_py3 import SecurityConfigurationRule
    from ._models_py3 import SecurityConfigurationRuleListResult
    from ._models_py3 import SubResource
    from ._models_py3 import SystemData
    from ._models_py3 import TagsObject
    from ._models_py3 import UserRule
    from ._models_py3 import UserRuleListResult
except (SyntaxError, ImportError):
    from ._models import ActiveConfiguration  # type: ignore
    from ._models import ActiveConfigurationListResult  # type: ignore
    from ._models import AddressPrefixItem  # type: ignore
    from ._models import AdminRule  # type: ignore
    from ._models import AdminRuleListResult  # type: ignore
    from ._models import AzureAsyncOperationResult  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import Components1Jq1T4ISchemasManagedserviceidentityPropertiesUserassignedidentitiesAdditionalproperties  # type: ignore
    from ._models import ConnectivityConfiguration  # type: ignore
    from ._models import ConnectivityConfigurationListResult  # type: ignore
    from ._models import ConnectivityGroupItem  # type: ignore
    from ._models import EffectiveConfiguration  # type: ignore
    from ._models import EffectiveVirtualNetwork  # type: ignore
    from ._models import EffectiveVirtualNetworksListResult  # type: ignore
    from ._models import EffectiveVirtualNetworksParameter  # type: ignore
    from ._models import Error  # type: ignore
    from ._models import ErrorDetails  # type: ignore
    from ._models import ExtendedLocation  # type: ignore
    from ._models import FailedImport  # type: ignore
    from ._models import GroupMembersItem  # type: ignore
    from ._models import ManagedServiceIdentity  # type: ignore
    from ._models import NetworkGroup  # type: ignore
    from ._models import NetworkGroupListResult  # type: ignore
    from ._models import NetworkManager  # type: ignore
    from ._models import NetworkManagerCommit  # type: ignore
    from ._models import NetworkManagerDeploymentStatus  # type: ignore
    from ._models import NetworkManagerDeploymentStatusListResult  # type: ignore
    from ._models import NetworkManagerDeploymentStatusParameter  # type: ignore
    from ._models import NetworkManagerEffectiveConfigurationListResult  # type: ignore
    from ._models import NetworkManagerListResult  # type: ignore
    from ._models import NetworkManagerPropertiesNetworkManagerScopes  # type: ignore
    from ._models import NetworkManagerSecurityConfigurationImport  # type: ignore
    from ._models import NetworkManagerSecurityGroupItem  # type: ignore
    from ._models import NetworkSecurityGroupImport  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import SecurityConfiguration  # type: ignore
    from ._models import SecurityConfigurationImportResult  # type: ignore
    from ._models import SecurityConfigurationListResult  # type: ignore
    from ._models import SecurityConfigurationRule  # type: ignore
    from ._models import SecurityConfigurationRuleListResult  # type: ignore
    from ._models import SubResource  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TagsObject  # type: ignore
    from ._models import UserRule  # type: ignore
    from ._models import UserRuleListResult  # type: ignore

from ._network_management_client_enums import (
    Access,
    AddressPrefixType,
    AuthenticationMethod,
    CommitType,
    ConfigType,
    ConnectivityTopology,
    CreatedByType,
    DeploymentStatus,
    DeploymentType,
    ExtendedLocationTypes,
    GroupConnectivity,
    IPAllocationMethod,
    IPVersion,
    MemberType,
    MembershipType,
    NetworkOperationStatus,
    ProvisioningState,
    ResourceIdentityType,
    ScopeAccesses,
    SecurityConfigurationRuleAccess,
    SecurityConfigurationRuleDirection,
    SecurityConfigurationRuleProtocol,
    SecurityType,
)

__all__ = [
    'ActiveConfiguration',
    'ActiveConfigurationListResult',
    'AddressPrefixItem',
    'AdminRule',
    'AdminRuleListResult',
    'AzureAsyncOperationResult',
    'CloudErrorBody',
    'Components1Jq1T4ISchemasManagedserviceidentityPropertiesUserassignedidentitiesAdditionalproperties',
    'ConnectivityConfiguration',
    'ConnectivityConfigurationListResult',
    'ConnectivityGroupItem',
    'EffectiveConfiguration',
    'EffectiveVirtualNetwork',
    'EffectiveVirtualNetworksListResult',
    'EffectiveVirtualNetworksParameter',
    'Error',
    'ErrorDetails',
    'ExtendedLocation',
    'FailedImport',
    'GroupMembersItem',
    'ManagedServiceIdentity',
    'NetworkGroup',
    'NetworkGroupListResult',
    'NetworkManager',
    'NetworkManagerCommit',
    'NetworkManagerDeploymentStatus',
    'NetworkManagerDeploymentStatusListResult',
    'NetworkManagerDeploymentStatusParameter',
    'NetworkManagerEffectiveConfigurationListResult',
    'NetworkManagerListResult',
    'NetworkManagerPropertiesNetworkManagerScopes',
    'NetworkManagerSecurityConfigurationImport',
    'NetworkManagerSecurityGroupItem',
    'NetworkSecurityGroupImport',
    'ProxyResource',
    'Resource',
    'SecurityConfiguration',
    'SecurityConfigurationImportResult',
    'SecurityConfigurationListResult',
    'SecurityConfigurationRule',
    'SecurityConfigurationRuleListResult',
    'SubResource',
    'SystemData',
    'TagsObject',
    'UserRule',
    'UserRuleListResult',
    'Access',
    'AddressPrefixType',
    'AuthenticationMethod',
    'CommitType',
    'ConfigType',
    'ConnectivityTopology',
    'CreatedByType',
    'DeploymentStatus',
    'DeploymentType',
    'ExtendedLocationTypes',
    'GroupConnectivity',
    'IPAllocationMethod',
    'IPVersion',
    'MemberType',
    'MembershipType',
    'NetworkOperationStatus',
    'ProvisioningState',
    'ResourceIdentityType',
    'ScopeAccesses',
    'SecurityConfigurationRuleAccess',
    'SecurityConfigurationRuleDirection',
    'SecurityConfigurationRuleProtocol',
    'SecurityType',
]
