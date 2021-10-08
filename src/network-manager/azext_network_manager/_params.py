# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    tags_type,
    get_three_state_flag,
    get_enum_type,
    resource_group_name_type,
    get_location_type
)
from azure.cli.core.commands.validators import get_default_location_from_resource_group
from azext_network_manager.action import (
    AddNetworkManagerScopes,
    AddConnectivityconfigurationsAppliesToGroups,
    AddGroupMembers,
    AddSecurityconfigurationsAppliesToGroups,
    AddNetworkSecurityGroupImports,
    AddSource,
    AddDestination
)


def load_arguments(self, _):

    # region network manager
    with self.argument_context('network manager') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', options_list=['--name', '-n', '--network-manager-name'], type=str,
                   help='The name of the network manager.', id_part='name')

    with self.argument_context('network manager list') as c:
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('network manager show') as c:
        c.argument('network_manager_name', options_list=['--name', '-n', '--network-manager-name'], type=str,
                   help='The name of the network manager.', id_part='name')

    with self.argument_context('network manager create') as c:
        c.argument('network_manager_name', options_list=['--name', '-n', '--network-manager-name'], type=str,
                   help='The name of the network manager.')
        c.argument('id_', options_list=['--id'], type=str, help='Resource ID.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('display_name', type=str, help='A friendly name for the network manager.')
        c.argument('description', type=str, help='A description of the network manager.')
        c.argument('network_manager_scopes', action=AddNetworkManagerScopes, nargs='+', help='Scope of Network '
                   'Manager.')
        c.argument('network_manager_scope_accesses', nargs='+', help='Scope Access. Available value: SecurityAdmin, '
                   'SecurityUser, Connectivity.')

    with self.argument_context('network manager update') as c:
        c.argument('network_manager_name', options_list=['--name', '-n', '--network-manager-name'], type=str,
                   help='The name of the network manager.', id_part='name')
        c.argument('id_', options_list=['--id'], type=str, help='Resource ID.')
        c.argument('location', arg_type=get_location_type(self.cli_ctx))
        c.argument('tags', tags_type)
        c.argument('display_name', type=str, help='A friendly name for the network manager.')
        c.argument('description', type=str, help='A description of the network manager.')
        c.argument('network_manager_scopes', action=AddNetworkManagerScopes, nargs='+', help='Scope of Network '
                   'Manager.')
        c.argument('network_manager_scope_accesses', nargs='+', help='Scope Access. Available value: SecurityAdmin, '
                   'SecurityUser, Connectivity.')
        c.ignore('parameters')

    with self.argument_context('network manager delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', options_list=['--name', '-n', '--network-manager-name'], type=str,
                   help='The name of the network manager.', id_part='name')

    # endregion
    with self.argument_context('network manager commit post') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('target_locations', nargs='+', help='List of target locations.')
        c.argument('configuration_ids', nargs='+', help='List of configuration ids.')
        c.argument('commit_type', arg_type=get_enum_type(['SecurityAdmin', 'SecurityUser', 'Connectivity']),
                   help='Commit Type.')

    with self.argument_context('network manager deploy-status list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')
        c.argument('regions', nargs='+', help='List of locations.')
        c.argument('deployment_types', nargs='+', help='List of configurations\' deployment types.')

    with self.argument_context('network manager effect-vnet list-by-network-group') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('network_group_name', type=str, help='The name of the network group to get.')
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('network manager effect-vnet list-by-network-manager') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')
        c.argument('conditional_members', type=str, help='Conditional Members.')

    with self.argument_context('network manager active-config list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')
        c.argument('region', type=str, help='Location name')

    with self.argument_context('network manager connect-config list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('network manager connect-config show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager connectivity configuration.',
                   id_part='child_name_1')

    with self.argument_context('network manager connect-config create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('configuration_name', type=str, help='The name of the network manager connectivity configuration.')
        c.argument('display_name', type=str, help='A friendly name for the resource.')
        c.argument('description', type=str, help='A description of the connectivity configuration.')
        c.argument('connectivity_topology', arg_type=get_enum_type(['HubAndSpokeTopology', 'MeshTopology']),
                   help='Connectivity topology type.')
        c.argument('hub_id', type=str, help='The hub vnet Id.')
        c.argument('is_global', arg_type=get_three_state_flag(), help='Flag if global mesh is supported.')
        c.argument('applies_to_groups', action=AddConnectivityconfigurationsAppliesToGroups, nargs='+', help='Groups '
                   'for configuration')
        c.argument('delete_existing_peering', arg_type=get_three_state_flag(), help='Flag if need to remove current '
                   'existing peerings.')

    with self.argument_context('network manager connect-config update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager connectivity configuration.',
                   id_part='child_name_1')
        c.argument('display_name', type=str, help='A friendly name for the resource.')
        c.argument('description', type=str, help='A description of the connectivity configuration.')
        c.argument('connectivity_topology', arg_type=get_enum_type(['HubAndSpokeTopology', 'MeshTopology']),
                   help='Connectivity topology type.')
        c.argument('hub_id', type=str, help='The hub vnet Id.')
        c.argument('is_global', arg_type=get_three_state_flag(), help='Flag if global mesh is supported.')
        c.argument('applies_to_groups', action=AddConnectivityconfigurationsAppliesToGroups, nargs='+', help='Groups '
                   'for configuration')
        c.argument('delete_existing_peering', arg_type=get_three_state_flag(), help='Flag if need to remove current '
                   'existing peerings.')
        c.ignore('connectivity_configuration')

    with self.argument_context('network manager connect-config delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager connectivity configuration.',
                   id_part='child_name_1')

    with self.argument_context('network manager group list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', options_list=['--network-manager-name'], type=str, help='The name of the network manager.')
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('network manager group show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', options_list=['--network-manager-name'], type=str, help='The name of the network manager.', id_part='name')
        c.argument('network_group_name', options_list=['--name', '-n', '--network-group-name'], type=str, help='The '
                   'name of the network group to get.', id_part='child_name_1')

    with self.argument_context('network manager group create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', options_list=['--network-manager-name'], type=str, help='The name of the network manager.')
        c.argument('network_group_name', options_list=['--name', '-n', '--network-group-name'], type=str, help='The '
                   'name of the network group to get.')
        c.argument('if_match', type=str, help='The ETag of the transformation. Omit this value to always overwrite the '
                   'current resource. Specify the last-seen ETag value to prevent accidentally overwriting concurrent '
                   'changes.')
        c.argument('display_name', type=str, help='A friendly name for the network group.')
        c.argument('description', type=str, help='A description of the network group.')
        c.argument('member_type', arg_type=get_enum_type(['VirtualNetwork', 'Subnet']), help='Group member type.')
        c.argument('group_members', action=AddGroupMembers, nargs='+', help='Group members of network group.')
        c.argument('conditional_membership', type=str, help='Network group conditional filter.')

    with self.argument_context('network manager group update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', options_list=['--network-manager-name'], type=str, help='The name of the network manager.', id_part='name')
        c.argument('network_group_name', options_list=['--name', '-n', '--network-group-name'], type=str, help='The '
                   'name of the network group to get.', id_part='child_name_1')
        c.argument('if_match', type=str, help='The ETag of the transformation. Omit this value to always overwrite the '
                   'current resource. Specify the last-seen ETag value to prevent accidentally overwriting concurrent '
                   'changes.')
        c.argument('display_name', type=str, help='A friendly name for the network group.')
        c.argument('description', type=str, help='A description of the network group.')
        c.argument('member_type', arg_type=get_enum_type(['VirtualNetwork', 'Subnet']), help='Group member type.')
        c.argument('group_members', action=AddGroupMembers, nargs='+', help='Group members of network group.')
        c.argument('conditional_membership', type=str, help='Network group conditional filter.')
        c.ignore('parameters')

    with self.argument_context('network manager group delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', options_list=['--network-manager-name'], type=str, help='The name of the network manager.', id_part='name')
        c.argument('network_group_name', options_list=['--name', '-n', '--network-group-name'], type=str, help='The '
                   'name of the network group to get.', id_part='child_name_1')

    with self.argument_context('network manager security-user-config list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('network manager security-user-config show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')

    with self.argument_context('network manager security-user-config create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.')
        c.argument('display_name', type=str, help='A display name of the security Configuration.')
        c.argument('description', type=str, help='A description of the security Configuration.')
        c.argument('security_type', arg_type=get_enum_type(['AdminPolicy', 'UserPolicy']), help='Security Type.')
        c.argument('delete_existing_ns_gs', arg_type=get_three_state_flag(), help='Flag if need to delete existing '
                   'network security groups.')

    with self.argument_context('network manager security-user-config update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')
        c.argument('display_name', type=str, help='A display name of the security Configuration.')
        c.argument('description', type=str, help='A description of the security Configuration.')
        c.argument('security_type', arg_type=get_enum_type(['AdminPolicy', 'UserPolicy']), help='Security Type.')
        c.argument('delete_existing_ns_gs', arg_type=get_three_state_flag(), help='Flag if need to delete existing '
                   'network security groups.')
        c.ignore('security_configuration')

    with self.argument_context('network manager security-user-config delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')

    with self.argument_context('network manager admin-rule list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.')
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('network manager security-admin-config list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('network manager security-admin-config show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')

    with self.argument_context('network manager security-admin-config create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.')
        c.argument('display_name', type=str, help='A display name of the security Configuration.')
        c.argument('description', type=str, help='A description of the security Configuration.')
        c.argument('security_type', arg_type=get_enum_type(['AdminPolicy', 'UserPolicy']), help='Security Type.')
        c.argument('delete_existing_ns_gs', arg_type=get_three_state_flag(), help='Flag if need to delete existing '
                   'network security groups.')

    with self.argument_context('network manager security-admin-config update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')
        c.argument('display_name', type=str, help='A display name of the security Configuration.')
        c.argument('description', type=str, help='A description of the security Configuration.')
        c.argument('security_type', arg_type=get_enum_type(['AdminPolicy', 'UserPolicy']), help='Security Type.')
        c.argument('delete_existing_ns_gs', arg_type=get_three_state_flag(), help='Flag if need to delete existing '
                   'network security groups.')
        c.ignore('security_configuration')

    with self.argument_context('network manager security-admin-config delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')

    with self.argument_context('network manager admin-rule collection create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')
        c.argument('rule_collection_name', type=str, help='The name of the admin rule collection.')
        c.argument('display_name', type=str, help='A friendly name for the rule.')
        c.argument('description', type=str, help='A description for this rule. Restricted to 140 chars.')
        c.argument('applies_to_groups', action=AddConnectivityconfigurationsAppliesToGroups, nargs='+', help='Groups '
                   'for configuration')

    with self.argument_context('network manager admin-rule collection update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')
        c.argument('rule_collection_name', type=str, help='The name of the admin rule collection.')
        c.argument('display_name', type=str, help='A friendly name for the rule.')
        c.argument('description', type=str, help='A description for this rule. Restricted to 140 chars.')
        c.argument('applies_to_groups', action=AddConnectivityconfigurationsAppliesToGroups, nargs='+', help='Groups '
                   'for configuration')

    with self.argument_context('network manager admin-rule collection list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('network manager admin-rule collection show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')
        c.argument('rule_collection_name', type=str, help='The name of the admin rule collection.')

    with self.argument_context('network manager admin-rule collection delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')
        c.argument('rule_collection_name', type=str, help='The name of the admin rule collection.')

    with self.argument_context('network manager admin-rule') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')
        c.argument('rule_name', type=str, help='The name of the rule.', id_part='child_name_2')
        c.argument('rule_collection_name', type=str, help='The name of the admin rule collection.')

    with self.argument_context('network manager admin-rule create') as c:
        c.argument('access', type=str, help='Indicates the access allowed for this particular rule.', arg_type=get_enum_type(['Allow', 'Deny', 'AlwaysAllow']))
        c.argument('flag', type=str, help='Default rule flag.')
        c.argument('kind', type=str, help='Required. Whether the rule is custom or default.Constant filled by server.', arg_type=get_enum_type(['Custom', 'Default']))
        c.argument('priority', type=int, help='The priority of the rule.')
        c.argument('sources', action=AddSource, nargs='+', help='The CIDR or source IP ranges.')
        c.argument('destinations', action=AddDestination, nargs='+', help='The destination address prefixes. CIDR or '
                   'destination IP ranges.')
        c.argument('display_name', type=str, help='A friendly name for the rule.')
        c.argument('description', type=str, help='A description for this rule. Restricted to 140 chars.')
        c.argument('protocol', arg_type=get_enum_type(['Tcp', 'Udp', 'Icmp', 'Esp', 'Any', 'Ah']), help='Network '
                   'protocol this rule applies to.')
        c.argument('source_port_ranges', nargs='+', help='The source port ranges.')
        c.argument('destination_port_ranges', nargs='+', help='The destination port ranges.')
        c.argument('direction', arg_type=get_enum_type(['Inbound', 'Outbound']), help='Indicates if the traffic '
                   'matched against the rule in inbound or outbound.')

    with self.argument_context('network manager admin-rule update') as c:
        c.argument('access', type=str, help='Indicates the access allowed for this particular rule.', arg_type=get_enum_type(['Allow', 'Deny', 'AlwaysAllow']))
        c.argument('flag', type=str, help='Default rule flag.')
        c.argument('kind', type=str, help='Required. Whether the rule is custom or default.Constant filled by server.', arg_type=get_enum_type(['Custom', 'Default']))
        c.argument('priority', type=int, help='The priority of the rule.')
        c.argument('sources', action=AddSource, nargs='+', help='The CIDR or source IP ranges.')
        c.argument('destinations', action=AddDestination, nargs='+', help='The destination address prefixes. CIDR or '
                   'destination IP ranges.')
        c.argument('display_name', type=str, help='A friendly name for the rule.')
        c.argument('description', type=str, help='A description for this rule. Restricted to 140 chars.')
        c.argument('protocol', arg_type=get_enum_type(['Tcp', 'Udp', 'Icmp', 'Esp', 'Any', 'Ah']), help='Network '
                   'protocol this rule applies to.')
        c.argument('source_port_ranges', nargs='+', help='The source port ranges.')
        c.argument('destination_port_ranges', nargs='+', help='The destination port ranges.')
        c.argument('direction', arg_type=get_enum_type(['Inbound', 'Outbound']), help='Indicates if the traffic '
                   'matched against the rule in inbound or outbound.')

    with self.argument_context('network manager user-rule list') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.')
        c.argument('top', type=int, help='An optional query parameter which specifies the maximum number of records to '
                   'be returned by the server.')
        c.argument('skip_token', type=str, help='SkipToken is only used if a previous operation returned a partial '
                   'result. If a previous response contains a nextLink element, the value of the nextLink element will '
                   'include a skipToken parameter that specifies a starting point to use for subsequent calls.')

    with self.argument_context('network manager user-rule show') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')
        c.argument('rule_name', type=str, help='The name of the rule.', id_part='child_name_2')

    with self.argument_context('network manager user-rule create') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.')
        c.argument('rule_name', type=str, help='The name of the rule.')
        c.argument('display_name', type=str, help='A friendly name for the rule.')
        c.argument('description', type=str, help='A description for this rule. Restricted to 140 chars.')
        c.argument('protocol', arg_type=get_enum_type(['Tcp', 'Udp', 'Icmp', 'Esp', 'Any', 'Ah']), help='Network '
                   'protocol this rule applies to.')
        c.argument('source', action=AddSource, nargs='+', help='The CIDR or source IP ranges.')
        c.argument('destination', action=AddDestination, nargs='+', help='The destination address prefixes. CIDR or '
                   'destination IP ranges.')
        c.argument('source_port_ranges', nargs='+', help='The source port ranges.')
        c.argument('destination_port_ranges', nargs='+', help='The destination port ranges.')
        c.argument('direction', arg_type=get_enum_type(['Inbound', 'Outbound']), help='Indicates if the traffic '
                   'matched against the rule in inbound or outbound.')

    with self.argument_context('network manager user-rule update') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')
        c.argument('rule_name', type=str, help='The name of the rule.', id_part='child_name_2')
        c.argument('display_name', type=str, help='A friendly name for the rule.')
        c.argument('description', type=str, help='A description for this rule. Restricted to 140 chars.')
        c.argument('protocol', arg_type=get_enum_type(['Tcp', 'Udp', 'Icmp', 'Esp', 'Any', 'Ah']), help='Network '
                   'protocol this rule applies to.')
        c.argument('source', action=AddSource, nargs='+', help='The CIDR or source IP ranges.')
        c.argument('destination', action=AddDestination, nargs='+', help='The destination address prefixes. CIDR or '
                   'destination IP ranges.')
        c.argument('source_port_ranges', nargs='+', help='The source port ranges.')
        c.argument('destination_port_ranges', nargs='+', help='The destination port ranges.')
        c.argument('direction', arg_type=get_enum_type(['Inbound', 'Outbound']), help='Indicates if the traffic '
                   'matched against the rule in inbound or outbound.')
        c.ignore('user_rule')

    with self.argument_context('network manager user-rule delete') as c:
        c.argument('resource_group_name', resource_group_name_type)
        c.argument('network_manager_name', type=str, help='The name of the network manager.', id_part='name')
        c.argument('configuration_name', type=str, help='The name of the network manager security Configuration.',
                   id_part='child_name_1')
        c.argument('rule_name', type=str, help='The name of the rule.', id_part='child_name_2')
