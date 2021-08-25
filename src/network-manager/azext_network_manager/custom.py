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
# pylint: disable=unused-argument


def network_manager_list(client,
                         resource_group_name,
                         top=None,
                         skip_token=None):
    return client.list(resource_group_name=resource_group_name,
                       top=top,
                       skip_token=skip_token)


def network_manager_show(client,
                         resource_group_name,
                         network_manager_name):
    return client.get(resource_group_name=resource_group_name,
                      network_manager_name=network_manager_name)


def network_manager_create(client,
                           resource_group_name,
                           network_manager_name,
                           id_=None,
                           location=None,
                           tags=None,
                           display_name=None,
                           description=None,
                           network_manager_scopes=None,
                           network_manager_scope_accesses=None):
    parameters = {}
    parameters['id'] = id_
    parameters['location'] = location
    parameters['tags'] = tags
    parameters['display_name'] = display_name
    parameters['description'] = description
    parameters['network_manager_scopes'] = network_manager_scopes
    parameters['network_manager_scope_accesses'] = network_manager_scope_accesses
    return client.create_or_update(resource_group_name=resource_group_name,
                                   network_manager_name=network_manager_name,
                                   parameters=parameters)


def network_manager_update(instance,
                           resource_group_name,
                           network_manager_name,
                           id_=None,
                           location=None,
                           tags=None,
                           display_name=None,
                           description=None,
                           network_manager_scopes=None,
                           network_manager_scope_accesses=None):
    if id_ is not None:
        instance.id = id_
    if location is not None:
        instance.location = location
    if tags is not None:
        instance.tags = tags
    if display_name is not None:
        instance.display_name = display_name
    if description is not None:
        instance.description = description
    if network_manager_scopes is not None:
        instance.network_manager_scopes = network_manager_scopes
    if network_manager_scope_accesses is not None:
        instance.network_manager_scope_accesses = network_manager_scope_accesses
    return instance


def network_manager_delete(client,
                           resource_group_name,
                           network_manager_name):
    return client.delete(resource_group_name=resource_group_name,
                         network_manager_name=network_manager_name)


def network_manager_commit_post(client,
                                resource_group_name,
                                network_manager_name,
                                target_locations=None,
                                configuration_ids=None,
                                commit_type=None):
    parameters = {}
    parameters['target_locations'] = target_locations
    parameters['configuration_ids'] = configuration_ids
    parameters['commit_type'] = commit_type
    return client.post(resource_group_name=resource_group_name,
                       network_manager_name=network_manager_name,
                       parameters=parameters)


def network_manager_deploy_status_list(client,
                                       resource_group_name,
                                       network_manager_name,
                                       top=None,
                                       skip_token=None,
                                       regions=None,
                                       deployment_types=None):
    parameters = {}
    parameters['regions'] = regions
    parameters['deployment_types'] = deployment_types
    return client.list(resource_group_name=resource_group_name,
                       network_manager_name=network_manager_name,
                       top=top,
                       skip_token=skip_token,
                       parameters=parameters)


def network_manager_effect_vnet_list_by_network_group(client,
                                                      resource_group_name,
                                                      network_manager_name,
                                                      network_group_name,
                                                      top=None,
                                                      skip_token=None):
    return client.list_by_network_group(resource_group_name=resource_group_name,
                                        network_manager_name=network_manager_name,
                                        network_group_name=network_group_name,
                                        top=top,
                                        skip_token=skip_token)


def network_manager_effect_vnet_list_by_network_manager(client,
                                                        resource_group_name,
                                                        network_manager_name,
                                                        top=None,
                                                        skip_token=None,
                                                        conditional_members=None):
    parameters = {}
    parameters['conditional_members'] = conditional_members
    return client.list_by_network_manager(resource_group_name=resource_group_name,
                                          network_manager_name=network_manager_name,
                                          top=top,
                                          skip_token=skip_token,
                                          parameters=parameters)


def network_manager_active_config_list(client,
                                       resource_group_name,
                                       network_manager_name,
                                       top=None,
                                       skip_token=None,
                                       region=None):
    return client.list(resource_group_name=resource_group_name,
                       network_manager_name=network_manager_name,
                       top=top,
                       skip_token=skip_token,
                       region=region)


def network_manager_connect_config_list(client,
                                        resource_group_name,
                                        network_manager_name,
                                        top=None,
                                        skip_token=None):
    return client.list(resource_group_name=resource_group_name,
                       network_manager_name=network_manager_name,
                       top=top,
                       skip_token=skip_token)


def network_manager_connect_config_show(client,
                                        resource_group_name,
                                        network_manager_name,
                                        configuration_name):
    return client.get(resource_group_name=resource_group_name,
                      network_manager_name=network_manager_name,
                      configuration_name=configuration_name)


def network_manager_connect_config_create(client,
                                          resource_group_name,
                                          network_manager_name,
                                          configuration_name,
                                          display_name=None,
                                          description=None,
                                          connectivity_topology=None,
                                          hub_id=None,
                                          is_global=None,
                                          applies_to_groups=None,
                                          delete_existing_peering=None):
    connectivity_configuration = {}
    connectivity_configuration['display_name'] = display_name
    connectivity_configuration['description'] = description
    connectivity_configuration['connectivity_topology'] = connectivity_topology
    connectivity_configuration['hub_id'] = hub_id
    connectivity_configuration['is_global'] = is_global
    connectivity_configuration['applies_to_groups'] = applies_to_groups
    connectivity_configuration['delete_existing_peering'] = delete_existing_peering
    return client.create_or_update(resource_group_name=resource_group_name,
                                   network_manager_name=network_manager_name,
                                   configuration_name=configuration_name,
                                   connectivity_configuration=connectivity_configuration)


def network_manager_connect_config_update(instance,
                                          resource_group_name,
                                          network_manager_name,
                                          configuration_name,
                                          display_name=None,
                                          description=None,
                                          connectivity_topology=None,
                                          hub_id=None,
                                          is_global=None,
                                          applies_to_groups=None,
                                          delete_existing_peering=None):
    if display_name is not None:
        instance.display_name = display_name
    if description is not None:
        instance.description = description
    if connectivity_topology is not None:
        instance.connectivity_topology = connectivity_topology
    if hub_id is not None:
        instance.hub_id = hub_id
    if is_global is not None:
        instance.is_global = is_global
    if applies_to_groups is not None:
        instance.applies_to_groups = applies_to_groups
    if delete_existing_peering is not None:
        instance.delete_existing_peering = delete_existing_peering
    return instance


def network_manager_connect_config_delete(client,
                                          resource_group_name,
                                          network_manager_name,
                                          configuration_name):
    return client.delete(resource_group_name=resource_group_name,
                         network_manager_name=network_manager_name,
                         configuration_name=configuration_name)


def network_effectiveconfiguration_list(client,
                                        resource_group_name,
                                        virtual_network_name,
                                        top=None,
                                        skip_token=None):
    return client.list(resource_group_name=resource_group_name,
                       virtual_network_name=virtual_network_name,
                       top=top,
                       skip_token=skip_token)


def network_manager_group_list(client,
                               resource_group_name,
                               network_manager_name,
                               top=None,
                               skip_token=None):
    return client.list(resource_group_name=resource_group_name,
                       network_manager_name=network_manager_name,
                       top=top,
                       skip_token=skip_token)


def network_manager_group_show(client,
                               resource_group_name,
                               network_manager_name,
                               network_group_name):
    return client.get(resource_group_name=resource_group_name,
                      network_manager_name=network_manager_name,
                      network_group_name=network_group_name)


def network_manager_group_create(client,
                                 resource_group_name,
                                 network_manager_name,
                                 network_group_name,
                                 if_match=None,
                                 display_name=None,
                                 description=None,
                                 member_type=None,
                                 group_members=None,
                                 conditional_membership=None):
    parameters = {}
    parameters['display_name'] = display_name
    parameters['description'] = description
    parameters['member_type'] = member_type
    parameters['group_members'] = group_members
    parameters['conditional_membership'] = conditional_membership
    return client.create_or_update(resource_group_name=resource_group_name,
                                   network_manager_name=network_manager_name,
                                   network_group_name=network_group_name,
                                   if_match=if_match,
                                   parameters=parameters)


def network_manager_group_update(instance,
                                 resource_group_name,
                                 network_manager_name,
                                 network_group_name,
                                 if_match=None,
                                 display_name=None,
                                 description=None,
                                 member_type=None,
                                 group_members=None,
                                 conditional_membership=None):
    if display_name is not None:
        instance.display_name = display_name
    if description is not None:
        instance.description = description
    if member_type is not None:
        instance.member_type = member_type
    if group_members is not None:
        instance.group_members = group_members
    if conditional_membership is not None:
        instance.conditional_membership = conditional_membership
    return instance


def network_manager_group_delete(client,
                                 resource_group_name,
                                 network_manager_name,
                                 network_group_name):
    return client.delete(resource_group_name=resource_group_name,
                         network_manager_name=network_manager_name,
                         network_group_name=network_group_name)


def network_manager_security_config_list(client,
                                         resource_group_name,
                                         network_manager_name,
                                         top=None,
                                         skip_token=None):
    return client.list(resource_group_name=resource_group_name,
                       network_manager_name=network_manager_name,
                       top=top,
                       skip_token=skip_token)


def network_manager_security_config_show(client,
                                         resource_group_name,
                                         network_manager_name,
                                         configuration_name):
    return client.get(resource_group_name=resource_group_name,
                      network_manager_name=network_manager_name,
                      configuration_name=configuration_name)


def network_manager_security_config_create(client,
                                           resource_group_name,
                                           network_manager_name,
                                           configuration_name,
                                           display_name=None,
                                           description=None,
                                           security_type=None,
                                           delete_existing_ns_gs=None,
                                           applies_to_groups=None):
    security_configuration = {}
    security_configuration['display_name'] = display_name
    security_configuration['description'] = description
    security_configuration['security_type'] = security_type
    security_configuration['delete_existing_ns_gs'] = delete_existing_ns_gs
    security_configuration['applies_to_groups'] = applies_to_groups
    return client.create_or_update(resource_group_name=resource_group_name,
                                   network_manager_name=network_manager_name,
                                   configuration_name=configuration_name,
                                   security_configuration=security_configuration)


def network_manager_security_config_update(instance,
                                           resource_group_name,
                                           network_manager_name,
                                           configuration_name,
                                           display_name=None,
                                           description=None,
                                           security_type=None,
                                           delete_existing_ns_gs=None,
                                           applies_to_groups=None):
    if display_name is not None:
        instance.display_name = display_name
    if description is not None:
        instance.description = description
    if security_type is not None:
        instance.security_type = security_type
    if delete_existing_ns_gs is not None:
        instance.delete_existing_ns_gs = delete_existing_ns_gs
    if applies_to_groups is not None:
        instance.applies_to_groups = applies_to_groups
    return instance


def network_manager_security_config_delete(client,
                                           resource_group_name,
                                           network_manager_name,
                                           configuration_name):
    return client.delete(resource_group_name=resource_group_name,
                         network_manager_name=network_manager_name,
                         configuration_name=configuration_name)


def network_manager_security_config_evaluate_import(client,
                                                    resource_group_name,
                                                    network_manager_name,
                                                    configuration_name,
                                                    top=None,
                                                    skip_token=None,
                                                    network_security_group_imports=None,
                                                    import_deny_rules_as_admin_rules=None,
                                                    admin_security_configuration_uri=None,
                                                    remove_allow_vnet_inbound_rule=None,
                                                    remove_allow_azure_load_balancer_inbound_rule=None,
                                                    remove_allow_vnet_outbound_rule=None,
                                                    remove_allow_internet_outbound_rule=None):
    parameters = {}
    parameters['network_security_group_imports'] = network_security_group_imports
    parameters['import_deny_rules_as_admin_rules'] = import_deny_rules_as_admin_rules
    parameters['admin_security_configuration_uri'] = admin_security_configuration_uri
    parameters['remove_allow_vnet_inbound_rule'] = remove_allow_vnet_inbound_rule
    parameters['remove_allow_azure_load_balancer_inbound_rule'] = remove_allow_azure_load_balancer_inbound_rule
    parameters['remove_allow_vnet_outbound_rule'] = remove_allow_vnet_outbound_rule
    parameters['remove_allow_internet_outbound_rule'] = remove_allow_internet_outbound_rule
    return client.evaluate_import(resource_group_name=resource_group_name,
                                  network_manager_name=network_manager_name,
                                  configuration_name=configuration_name,
                                  top=top,
                                  skip_token=skip_token,
                                  parameters=parameters)


def network_manager_security_config_import(client,
                                           resource_group_name,
                                           network_manager_name,
                                           configuration_name,
                                           network_security_group_imports=None,
                                           import_deny_rules_as_admin_rules=None,
                                           admin_security_configuration_uri=None,
                                           remove_allow_vnet_inbound_rule=None,
                                           remove_allow_azure_load_balancer_inbound_rule=None,
                                           remove_allow_vnet_outbound_rule=None,
                                           remove_allow_internet_outbound_rule=None):
    parameters = {}
    parameters['network_security_group_imports'] = network_security_group_imports
    parameters['import_deny_rules_as_admin_rules'] = import_deny_rules_as_admin_rules
    parameters['admin_security_configuration_uri'] = admin_security_configuration_uri
    parameters['remove_allow_vnet_inbound_rule'] = remove_allow_vnet_inbound_rule
    parameters['remove_allow_azure_load_balancer_inbound_rule'] = remove_allow_azure_load_balancer_inbound_rule
    parameters['remove_allow_vnet_outbound_rule'] = remove_allow_vnet_outbound_rule
    parameters['remove_allow_internet_outbound_rule'] = remove_allow_internet_outbound_rule
    return client.import_method(resource_group_name=resource_group_name,
                                network_manager_name=network_manager_name,
                                configuration_name=configuration_name,
                                parameters=parameters)


def network_manager_admin_rule_list(client,
                                    resource_group_name,
                                    network_manager_name,
                                    configuration_name,
                                    top=None,
                                    skip_token=None):
    return client.list(resource_group_name=resource_group_name,
                       network_manager_name=network_manager_name,
                       configuration_name=configuration_name,
                       top=top,
                       skip_token=skip_token)


def network_manager_admin_rule_show(client,
                                    resource_group_name,
                                    network_manager_name,
                                    configuration_name,
                                    rule_name):
    return client.get(resource_group_name=resource_group_name,
                      network_manager_name=network_manager_name,
                      configuration_name=configuration_name,
                      rule_name=rule_name)


def network_manager_admin_rule_delete(client,
                                      resource_group_name,
                                      network_manager_name,
                                      configuration_name,
                                      rule_name):
    return client.delete(resource_group_name=resource_group_name,
                         network_manager_name=network_manager_name,
                         configuration_name=configuration_name,
                         rule_name=rule_name)


def network_manager_user_rule_list(client,
                                   resource_group_name,
                                   network_manager_name,
                                   configuration_name,
                                   top=None,
                                   skip_token=None):
    return client.list(resource_group_name=resource_group_name,
                       network_manager_name=network_manager_name,
                       configuration_name=configuration_name,
                       top=top,
                       skip_token=skip_token)


def network_manager_user_rule_show(client,
                                   resource_group_name,
                                   network_manager_name,
                                   configuration_name,
                                   rule_name):
    return client.get(resource_group_name=resource_group_name,
                      network_manager_name=network_manager_name,
                      configuration_name=configuration_name,
                      rule_name=rule_name)


def network_manager_user_rule_create(client,
                                     resource_group_name,
                                     network_manager_name,
                                     configuration_name,
                                     rule_name,
                                     display_name=None,
                                     description=None,
                                     protocol=None,
                                     source=None,
                                     destination=None,
                                     source_port_ranges=None,
                                     destination_port_ranges=None,
                                     direction=None):
    user_rule = {}
    user_rule['display_name'] = display_name
    user_rule['description'] = description
    user_rule['protocol'] = protocol
    user_rule['source'] = source
    user_rule['destination'] = destination
    user_rule['source_port_ranges'] = source_port_ranges
    user_rule['destination_port_ranges'] = destination_port_ranges
    user_rule['direction'] = direction
    return client.create_or_update(resource_group_name=resource_group_name,
                                   network_manager_name=network_manager_name,
                                   configuration_name=configuration_name,
                                   rule_name=rule_name,
                                   user_rule=user_rule)


def network_manager_user_rule_update(instance,
                                     resource_group_name,
                                     network_manager_name,
                                     configuration_name,
                                     rule_name,
                                     display_name=None,
                                     description=None,
                                     protocol=None,
                                     source=None,
                                     destination=None,
                                     source_port_ranges=None,
                                     destination_port_ranges=None,
                                     direction=None):
    if display_name is not None:
        instance.display_name = display_name
    if description is not None:
        instance.description = description
    if protocol is not None:
        instance.protocol = protocol
    if source is not None:
        instance.source = source
    if destination is not None:
        instance.destination = destination
    if source_port_ranges is not None:
        instance.source_port_ranges = source_port_ranges
    if destination_port_ranges is not None:
        instance.destination_port_ranges = destination_port_ranges
    if direction is not None:
        instance.direction = direction
    return instance


def network_manager_user_rule_delete(client,
                                     resource_group_name,
                                     network_manager_name,
                                     configuration_name,
                                     rule_name):
    return client.delete(resource_group_name=resource_group_name,
                         network_manager_name=network_manager_name,
                         configuration_name=configuration_name,
                         rule_name=rule_name)