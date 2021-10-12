# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType
from azext_network_manager._client_factory import (
    cf_networkmanager, cf_networkmanagercommit, cf_networkmanagerdeploymentstatus, cf_effectivevirtualnetwork,
    cf_activeconnectivityconfiguration, cf_connectivityconfiguration, cf_networkgroup, cf_userrule,
    cf_userrulecollection, cf_adminrule, cf_adminrulecollection, cf_securityadminconfiguration, cf_securityuserconfiguration,
    cf_activesecurityadminrule, cf_activesecurityuserrule, cf_effectiveconnectivityconfiguration, cf_effectivesecurityadminrule)


def load_command_table(self, _):
    network_networkmanager = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._network_managers_operations#NetworkManagersOperations.{}',
        client_factory=cf_networkmanager
    )

    network_networkmanagercommit = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._network_manager_commits_operations#NetworkManagercommitsOperations.{}',
        client_factory=cf_networkmanagercommit
    )

    network_networkmanagerdeploymentstatus = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._network_manager_deployment_status_operations#NetworkManagerDeploymentStatusOperations.{}',
        client_factory=cf_networkmanagerdeploymentstatus
    )

    network_effectivevirtualnetwork = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._effective_virtual_networks_operations#EffectiveVirtualNetworksOperations.{}',
        client_factory=cf_effectivevirtualnetwork)

    network_activeconnectivityconfiguration = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._active_connectivity_configurations_operations#ActiveConnetivityConfigurationsOperations.{}',
        client_factory=cf_activeconnectivityconfiguration
    )

    network_effectiveconnectivityconfiguration = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._effective_connectivity_configurations_operations#EffectiveConnetivityConfigurationsOperations.{}',
        client_factory=cf_effectiveconnectivityconfiguration
    )

    network_activesecurityadminrule = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._active_security_admin_rules_operations#ActiveSecurityAdminRulesOperations.{}',
        client_factory=cf_activesecurityadminrule
    )

    network_activesecurityuserrule = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._active_security_user_rules_operations#ActiveSecurityUserRulesOperations.{}',
        client_factory=cf_activesecurityuserrule
    )

    network_connectivityconfiguration = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._connectivity_configurations_operations#ConnectivityConfigurationsOperations.{}',
        client_factory=cf_connectivityconfiguration
    )

    network_networkgroup = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._network_groups_operations#NetworkGroupsOperations.{}',
        client_factory=cf_networkgroup
    )

    network_securityuserconfiguration = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._security_user_configurations_operations#SecurityUserConfigurationsOperations.{}',
        client_factory=cf_securityuserconfiguration
    )

    network_securityadminconfiguration = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._security_admin_configurations_operations#SecurityAdminConfigurationsOperations.{}',
        client_factory=cf_securityadminconfiguration
    )

    network_adminrule = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._admin_rules_operations#AdminRulesOperations.{}',
        client_factory=cf_adminrule
    )

    network_adminrulecollection = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._admin_rule_collections_operations#AdminRuleCollectionsOperations.{}',
        client_factory=cf_adminrulecollection
    )

    network_userrule = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._user_rules_operations#UserRulesOperations.{}',
        client_factory=cf_userrule
    )

    network_userrulecollection = CliCommandType(
        operations_tmpl='azext_network_manager.vendored_sdks.operations._user_rule_collections_operations#UserRuleCollectionsOperations.{}',
        client_factory=cf_userrulecollection
    )

    with self.command_group('network manager', network_networkmanager, client_factory=cf_networkmanager) as g:
        g.custom_command('create', 'network_manager_create')
        g.custom_command('list', 'network_manager_list')
        g.custom_show_command('show', 'network_manager_show')
        g.generic_update_command('update', custom_func_name='network_manager_update')
        g.custom_command('delete', 'network_manager_delete', confirmation=True)

    with self.command_group('network manager commit', network_networkmanagercommit, client_factory=cf_networkmanagercommit) as g:
        g.custom_command('post', 'network_manager_commit_post')

    with self.command_group('network manager deploy-status', network_networkmanagerdeploymentstatus, client_factory=cf_networkmanagerdeploymentstatus) as g:
        g.custom_command('list', 'network_manager_deploy_status_list')

    with self.command_group('network manager effect-vnet', network_effectivevirtualnetwork, client_factory=cf_effectivevirtualnetwork) as g:
        g.custom_command('list-by-network-group', 'network_manager_effect_vnet_list_by_network_group')
        g.custom_command('list-by-network-manager', 'network_manager_effect_vnet_list_by_network_manager')

    with self.command_group('network manager active-config', network_activeconnectivityconfiguration, client_factory=cf_activeconnectivityconfiguration) as g:
        g.custom_command('list', 'network_manager_active_config_list')

    with self.command_group('network manager effective-config', network_effectiveconnectivityconfiguration, client_factory=cf_effectiveconnectivityconfiguration) as g:
        g.custom_command('list', 'network_manager_effective_config_list')

    with self.command_group('network manager active-security-admin-rule', network_activesecurityadminrule, client_factory=cf_activesecurityadminrule) as g:
        g.custom_command('list', 'network_manager_active_security_admin_rule_list')

    with self.command_group('network manager active-security-user-rule', network_activesecurityuserrule, client_factory=cf_activesecurityuserrule) as g:
        g.custom_command('list', 'network_manager_active_security_user_rule_list')

    with self.command_group('network manager connect-config', network_connectivityconfiguration, client_factory=cf_connectivityconfiguration) as g:
        g.custom_command('list', 'network_manager_connect_config_list')
        g.custom_show_command('show', 'network_manager_connect_config_show')
        g.custom_command('create', 'network_manager_connect_config_create')
        g.generic_update_command('update', setter_arg_name='connectivity_configuration', custom_func_name='network_manager_connect_config_update')
        g.custom_command('delete', 'network_manager_connect_config_delete', confirmation=True)

    with self.command_group('network manager group', network_networkgroup, client_factory=cf_networkgroup) as g:
        g.custom_command('list', 'network_manager_group_list')
        g.custom_show_command('show', 'network_manager_group_show')
        g.custom_command('create', 'network_manager_group_create')
        g.generic_update_command('update', custom_func_name='network_manager_group_update')
        g.custom_command('delete', 'network_manager_group_delete', confirmation=True)

    with self.command_group('network manager security-user-config', network_securityuserconfiguration, client_factory=cf_securityuserconfiguration) as g:
        g.custom_command('list', 'network_manager_security_user_config_list')
        g.custom_show_command('show', 'network_manager_security_user_config_show')
        g.custom_command('create', 'network_manager_security_user_config_create')
        g.generic_update_command('update', setter_arg_name='security_user_configuration', custom_func_name='network_manager_security_user_config_update')
        g.custom_command('delete', 'network_manager_security_user_config_delete', confirmation=True)

    with self.command_group('network manager security-admin-config', network_securityadminconfiguration, client_factory=cf_securityadminconfiguration) as g:
        g.custom_command('list', 'network_manager_security_admin_config_list')
        g.custom_show_command('show', 'network_manager_security_admin_config_show')
        g.custom_command('create', 'network_manager_security_admin_config_create')
        g.generic_update_command('update', setter_arg_name='security_admin_configuration', custom_func_name='network_manager_security_admin_config_update')
        g.custom_command('delete', 'network_manager_security_admin_config_delete', confirmation=True)

    with self.command_group('network manager admin-rule', network_adminrule, client_factory=cf_adminrule) as g:
        g.custom_command('create', 'network_manager_admin_rule_create')
        g.generic_update_command('update', setter_arg_name='admin_rule', custom_func_name='network_manager_admin_rule_update')
        g.custom_command('list', 'network_manager_admin_rule_list')
        g.custom_show_command('show', 'network_manager_admin_rule_show')
        g.custom_command('delete', 'network_manager_admin_rule_delete', confirmation=True)

    with self.command_group('network manager admin-rule collection', network_adminrulecollection, client_factory=cf_adminrulecollection) as g:
        g.custom_command('create', 'network_manager_admin_rule_collection_create')
        g.generic_update_command('update', setter_arg_name='rule_collection', custom_func_name='network_manager_admin_rule_collection_update')
        g.custom_command('list', 'network_manager_admin_rule_collection_list')
        g.custom_show_command('show', 'network_manager_admin_rule_collection_show')
        g.custom_command('delete', 'network_manager_admin_rule_collection_delete', confirmation=True)

    with self.command_group('network manager user-rule', network_userrule, client_factory=cf_userrule) as g:
        g.custom_command('list', 'network_manager_user_rule_list')
        g.custom_show_command('show', 'network_manager_user_rule_show')
        g.custom_command('create', 'network_manager_user_rule_create')
        g.generic_update_command('update', setter_arg_name='user_rule', custom_func_name='network_manager_user_rule_update')
        g.custom_command('delete', 'network_manager_user_rule_delete', confirmation=True)

    with self.command_group('network manager user-rule collection', network_userrulecollection, client_factory=cf_userrulecollection) as g:
        g.custom_command('create', 'network_manager_user_rule_collection_create')
        g.generic_update_command('update', setter_arg_name='user_rule_collection', custom_func_name='network_manager_user_rule_collection_update')
        g.custom_command('list', 'network_manager_user_rule_collection_list')
        g.custom_show_command('show', 'network_manager_user_rule_collection_show')
        g.custom_command('delete', 'network_manager_user_rule_collection_delete', confirmation=True)