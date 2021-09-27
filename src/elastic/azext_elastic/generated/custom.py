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

from azure.cli.core.util import sdk_no_wait


def elastic_monitor_list(client,
                         resource_group_name=None):
    if resource_group_name:
        return client.list_by_resource_group(resource_group_name=resource_group_name)
    return client.list()


def elastic_monitor_show(client,
                         resource_group_name,
                         monitor_name):
    return client.get(resource_group_name=resource_group_name,
                      monitor_name=monitor_name)


def elastic_monitor_create(client,
                           resource_group_name,
                           monitor_name,
                           location,
                           tags=None,
                           provisioning_state=None,
                           monitoring_status=None,
                           elastic_properties=None,
                           user_info=None,
                           sku=None,
                           no_wait=False):
    body = {}
    if tags is not None:
        body['tags'] = tags
    body['location'] = location
    body['identity'] = {}
    body['identity']['type'] = "SystemAssigned"
    if len(body['identity']) == 0:
        del body['identity']
    body['properties'] = {}
    if provisioning_state is not None:
        body['properties']['provisioning_state'] = provisioning_state
    if monitoring_status is not None:
        body['properties']['monitoring_status'] = monitoring_status
    if elastic_properties is not None:
        body['properties']['elastic_properties'] = elastic_properties
    if user_info is not None:
        body['properties']['user_info'] = user_info
    if len(body['properties']) == 0:
        del body['properties']
    body['sku'] = {}
    if sku is not None:
        body['sku']['name'] = sku
    if len(body['sku']) == 0:
        del body['sku']
    return sdk_no_wait(no_wait,
                       client.begin_create,
                       resource_group_name=resource_group_name,
                       monitor_name=monitor_name,
                       body=body)


def elastic_monitor_update(client,
                           resource_group_name,
                           monitor_name,
                           tags=None):
    body = {}
    if tags is not None:
        body['tags'] = tags
    return client.update(resource_group_name=resource_group_name,
                         monitor_name=monitor_name,
                         body=body)


def elastic_monitor_delete(client,
                           resource_group_name,
                           monitor_name,
                           no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       monitor_name=monitor_name)


def elastic_monitored_resource_list(client,
                                    resource_group_name,
                                    monitor_name):
    return client.list(resource_group_name=resource_group_name,
                       monitor_name=monitor_name)


def elastic_deployment_info_list(client,
                                 resource_group_name,
                                 monitor_name):
    return client.list(resource_group_name=resource_group_name,
                       monitor_name=monitor_name)


def elastic_tag_rule_list(client,
                          resource_group_name,
                          monitor_name):
    return client.list(resource_group_name=resource_group_name,
                       monitor_name=monitor_name)


def elastic_tag_rule_show(client,
                          resource_group_name,
                          monitor_name,
                          rule_set_name):
    return client.get(resource_group_name=resource_group_name,
                      monitor_name=monitor_name,
                      rule_set_name=rule_set_name)


def elastic_tag_rule_create(client,
                            resource_group_name,
                            monitor_name,
                            rule_set_name,
                            provisioning_state=None,
                            send_aad_logs=None,
                            send_subscription_logs=None,
                            send_activity_logs=None,
                            filtering_tags=None):
    body = {}
    body['properties'] = {}
    if provisioning_state is not None:
        body['properties']['provisioning_state'] = provisioning_state
    body['properties']['log_rules'] = {}
    if send_aad_logs is not None:
        body['properties']['log_rules']['send_aad_logs'] = send_aad_logs
    if send_subscription_logs is not None:
        body['properties']['log_rules']['send_subscription_logs'] = send_subscription_logs
    if send_activity_logs is not None:
        body['properties']['log_rules']['send_activity_logs'] = send_activity_logs
    if filtering_tags is not None:
        body['properties']['log_rules']['filtering_tags'] = filtering_tags
    if len(body['properties']['log_rules']) == 0:
        del body['properties']['log_rules']
    return client.create_or_update(resource_group_name=resource_group_name,
                                   monitor_name=monitor_name,
                                   rule_set_name=rule_set_name,
                                   body=body)


def elastic_tag_rule_update(instance,
                            resource_group_name,
                            monitor_name,
                            rule_set_name,
                            provisioning_state=None,
                            send_aad_logs=None,
                            send_subscription_logs=None,
                            send_activity_logs=None,
                            filtering_tags=None):
    if provisioning_state is not None:
        instance.properties.provisioning_state = provisioning_state
    if send_aad_logs is not None:
        instance.properties.log_rules.send_aad_logs = send_aad_logs
    if send_subscription_logs is not None:
        instance.properties.log_rules.send_subscription_logs = send_subscription_logs
    if send_activity_logs is not None:
        instance.properties.log_rules.send_activity_logs = send_activity_logs
    if filtering_tags is not None:
        instance.properties.log_rules.filtering_tags = filtering_tags
    return instance


def elastic_tag_rule_delete(client,
                            resource_group_name,
                            monitor_name,
                            rule_set_name,
                            no_wait=False):
    return sdk_no_wait(no_wait,
                       client.begin_delete,
                       resource_group_name=resource_group_name,
                       monitor_name=monitor_name,
                       rule_set_name=rule_set_name)


def elastic_vm_host_list(client,
                         resource_group_name,
                         monitor_name):
    return client.list(resource_group_name=resource_group_name,
                       monitor_name=monitor_name)


def elastic_vm_ingestion_detail(client,
                                resource_group_name,
                                monitor_name):
    return client.details(resource_group_name=resource_group_name,
                          monitor_name=monitor_name)


def elastic_vm_collection_update(client,
                                 resource_group_name,
                                 monitor_name,
                                 vm_resource_id=None,
                                 operation_name=None):
    body = {}
    if vm_resource_id is not None:
        body['vm_resource_id'] = vm_resource_id
    if operation_name is not None:
        body['operation_name'] = operation_name
    return client.update(resource_group_name=resource_group_name,
                         monitor_name=monitor_name,
                         body=body)
