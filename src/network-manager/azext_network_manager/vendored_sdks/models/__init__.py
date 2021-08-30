# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import ActiveBaseSecurityAdminRule
    from ._models_py3 import ActiveBaseSecurityUserRule
    from ._models_py3 import ActiveConfigurationParameter
    from ._models_py3 import ActiveConnectivityConfiguration
    from ._models_py3 import ActiveConnectivityConfigurationsListResult
    from ._models_py3 import ActiveDefaultSecurityAdminRule
    from ._models_py3 import ActiveDefaultSecurityUserRule
    from ._models_py3 import ActiveSecurityAdminRule
    from ._models_py3 import ActiveSecurityAdminRulesListResult
    from ._models_py3 import ActiveSecurityUserRule
    from ._models_py3 import ActiveSecurityUserRulesListResult
    from ._models_py3 import AddressPrefixItem
    from ._models_py3 import AdminRule
    from ._models_py3 import AdminRuleListResult
    from ._models_py3 import BaseAdminRule
    from ._models_py3 import BaseUserRule
    from ._models_py3 import CloudErrorBody
    from ._models_py3 import ConfigurationGroup
    from ._models_py3 import ConnectivityConfiguration
    from ._models_py3 import ConnectivityConfigurationListResult
    from ._models_py3 import ConnectivityGroupItem
    from ._models_py3 import DefaultAdminRule
    from ._models_py3 import DefaultUserRule
    from ._models_py3 import EffectiveBaseSecurityAdminRule
    from ._models_py3 import EffectiveConnectivityConfiguration
    from ._models_py3 import EffectiveDefaultSecurityAdminRule
    from ._models_py3 import EffectiveSecurityAdminRule
    from ._models_py3 import EffectiveVirtualNetwork
    from ._models_py3 import EffectiveVirtualNetworksListResult
    from ._models_py3 import EffectiveVirtualNetworksParameter
    from ._models_py3 import GroupMembersItem
    from ._models_py3 import NetworkGroup
    from ._models_py3 import NetworkGroupListResult
    from ._models_py3 import NetworkManager
    from ._models_py3 import NetworkManagerCommit
    from ._models_py3 import NetworkManagerDeploymentStatus
    from ._models_py3 import NetworkManagerDeploymentStatusListResult
    from ._models_py3 import NetworkManagerDeploymentStatusParameter
    from ._models_py3 import NetworkManagerEffectiveConnectivityConfigurationListResult
    from ._models_py3 import NetworkManagerEffectiveSecurityAdminRulesListResult
    from ._models_py3 import NetworkManagerListResult
    from ._models_py3 import NetworkManagerPropertiesNetworkManagerScopes
    from ._models_py3 import NetworkManagerSecurityGroupItem
    from ._models_py3 import NetworkSecurityPerimeter
    from ._models_py3 import NetworkSecurityPerimeterListResult
    from ._models_py3 import PerimeterAssociableResource
    from ._models_py3 import PerimeterAssociableResourcesListResult
    from ._models_py3 import ProxyResource
    from ._models_py3 import QueryRequestOptions
    from ._models_py3 import Resource
    from ._models_py3 import RuleCollection
    from ._models_py3 import RuleCollectionListResult
    from ._models_py3 import SecurityConfiguration
    from ._models_py3 import SecurityConfigurationListResult
    from ._models_py3 import SystemData
    from ._models_py3 import TagsObject
    from ._models_py3 import UserRule
    from ._models_py3 import UserRuleListResult
except (SyntaxError, ImportError):
    from ._models import ActiveBaseSecurityAdminRule  # type: ignore
    from ._models import ActiveBaseSecurityUserRule  # type: ignore
    from ._models import ActiveConfigurationParameter  # type: ignore
    from ._models import ActiveConnectivityConfiguration  # type: ignore
    from ._models import ActiveConnectivityConfigurationsListResult  # type: ignore
    from ._models import ActiveDefaultSecurityAdminRule  # type: ignore
    from ._models import ActiveDefaultSecurityUserRule  # type: ignore
    from ._models import ActiveSecurityAdminRule  # type: ignore
    from ._models import ActiveSecurityAdminRulesListResult  # type: ignore
    from ._models import ActiveSecurityUserRule  # type: ignore
    from ._models import ActiveSecurityUserRulesListResult  # type: ignore
    from ._models import AddressPrefixItem  # type: ignore
    from ._models import AdminRule  # type: ignore
    from ._models import AdminRuleListResult  # type: ignore
    from ._models import BaseAdminRule  # type: ignore
    from ._models import BaseUserRule  # type: ignore
    from ._models import CloudErrorBody  # type: ignore
    from ._models import ConfigurationGroup  # type: ignore
    from ._models import ConnectivityConfiguration  # type: ignore
    from ._models import ConnectivityConfigurationListResult  # type: ignore
    from ._models import ConnectivityGroupItem  # type: ignore
    from ._models import DefaultAdminRule  # type: ignore
    from ._models import DefaultUserRule  # type: ignore
    from ._models import EffectiveBaseSecurityAdminRule  # type: ignore
    from ._models import EffectiveConnectivityConfiguration  # type: ignore
    from ._models import EffectiveDefaultSecurityAdminRule  # type: ignore
    from ._models import EffectiveSecurityAdminRule  # type: ignore
    from ._models import EffectiveVirtualNetwork  # type: ignore
    from ._models import EffectiveVirtualNetworksListResult  # type: ignore
    from ._models import EffectiveVirtualNetworksParameter  # type: ignore
    from ._models import GroupMembersItem  # type: ignore
    from ._models import NetworkGroup  # type: ignore
    from ._models import NetworkGroupListResult  # type: ignore
    from ._models import NetworkManager  # type: ignore
    from ._models import NetworkManagerCommit  # type: ignore
    from ._models import NetworkManagerDeploymentStatus  # type: ignore
    from ._models import NetworkManagerDeploymentStatusListResult  # type: ignore
    from ._models import NetworkManagerDeploymentStatusParameter  # type: ignore
    from ._models import NetworkManagerEffectiveConnectivityConfigurationListResult  # type: ignore
    from ._models import NetworkManagerEffectiveSecurityAdminRulesListResult  # type: ignore
    from ._models import NetworkManagerListResult  # type: ignore
    from ._models import NetworkManagerPropertiesNetworkManagerScopes  # type: ignore
    from ._models import NetworkManagerSecurityGroupItem  # type: ignore
    from ._models import NetworkSecurityPerimeter  # type: ignore
    from ._models import NetworkSecurityPerimeterListResult  # type: ignore
    from ._models import PerimeterAssociableResource  # type: ignore
    from ._models import PerimeterAssociableResourcesListResult  # type: ignore
    from ._models import ProxyResource  # type: ignore
    from ._models import QueryRequestOptions  # type: ignore
    from ._models import Resource  # type: ignore
    from ._models import RuleCollection  # type: ignore
    from ._models import RuleCollectionListResult  # type: ignore
    from ._models import SecurityConfiguration  # type: ignore
    from ._models import SecurityConfigurationListResult  # type: ignore
    from ._models import SystemData  # type: ignore
    from ._models import TagsObject  # type: ignore
    from ._models import UserRule  # type: ignore
    from ._models import UserRuleListResult  # type: ignore

from ._network_management_client_enums import (
    AddressPrefixType,
    AdminRuleKind,
    ConfigurationType,
    ConnectivityTopology,
    CreatedByType,
    DeleteExistingNSGs,
    DeleteExistingPeering,
    DeploymentStatus,
    EffectiveAdminRuleKind,
    EffectiveUserRuleKind,
    GroupConnectivity,
    IsGlobal,
    MemberType,
    MembershipType,
    ProvisioningState,
    SecurityConfigurationRuleAccess,
    SecurityConfigurationRuleDirection,
    SecurityConfigurationRuleProtocol,
    SecurityType,
    UseHubGateway,
    UserRuleKind,
)

__all__ = [
    'ActiveBaseSecurityAdminRule',
    'ActiveBaseSecurityUserRule',
    'ActiveConfigurationParameter',
    'ActiveConnectivityConfiguration',
    'ActiveConnectivityConfigurationsListResult',
    'ActiveDefaultSecurityAdminRule',
    'ActiveDefaultSecurityUserRule',
    'ActiveSecurityAdminRule',
    'ActiveSecurityAdminRulesListResult',
    'ActiveSecurityUserRule',
    'ActiveSecurityUserRulesListResult',
    'AddressPrefixItem',
    'AdminRule',
    'AdminRuleListResult',
    'BaseAdminRule',
    'BaseUserRule',
    'CloudErrorBody',
    'ConfigurationGroup',
    'ConnectivityConfiguration',
    'ConnectivityConfigurationListResult',
    'ConnectivityGroupItem',
    'DefaultAdminRule',
    'DefaultUserRule',
    'EffectiveBaseSecurityAdminRule',
    'EffectiveConnectivityConfiguration',
    'EffectiveDefaultSecurityAdminRule',
    'EffectiveSecurityAdminRule',
    'EffectiveVirtualNetwork',
    'EffectiveVirtualNetworksListResult',
    'EffectiveVirtualNetworksParameter',
    'GroupMembersItem',
    'NetworkGroup',
    'NetworkGroupListResult',
    'NetworkManager',
    'NetworkManagerCommit',
    'NetworkManagerDeploymentStatus',
    'NetworkManagerDeploymentStatusListResult',
    'NetworkManagerDeploymentStatusParameter',
    'NetworkManagerEffectiveConnectivityConfigurationListResult',
    'NetworkManagerEffectiveSecurityAdminRulesListResult',
    'NetworkManagerListResult',
    'NetworkManagerPropertiesNetworkManagerScopes',
    'NetworkManagerSecurityGroupItem',
    'NetworkSecurityPerimeter',
    'NetworkSecurityPerimeterListResult',
    'PerimeterAssociableResource',
    'PerimeterAssociableResourcesListResult',
    'ProxyResource',
    'QueryRequestOptions',
    'Resource',
    'RuleCollection',
    'RuleCollectionListResult',
    'SecurityConfiguration',
    'SecurityConfigurationListResult',
    'SystemData',
    'TagsObject',
    'UserRule',
    'UserRuleListResult',
    'AddressPrefixType',
    'AdminRuleKind',
    'ConfigurationType',
    'ConnectivityTopology',
    'CreatedByType',
    'DeleteExistingNSGs',
    'DeleteExistingPeering',
    'DeploymentStatus',
    'EffectiveAdminRuleKind',
    'EffectiveUserRuleKind',
    'GroupConnectivity',
    'IsGlobal',
    'MemberType',
    'MembershipType',
    'ProvisioningState',
    'SecurityConfigurationRuleAccess',
    'SecurityConfigurationRuleDirection',
    'SecurityConfigurationRuleProtocol',
    'SecurityType',
    'UseHubGateway',
    'UserRuleKind',
]
