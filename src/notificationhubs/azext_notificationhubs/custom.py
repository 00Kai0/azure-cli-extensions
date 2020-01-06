# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-statements
# pylint: disable=too-many-lines
# pylint: disable=too-many-locals
# pylint: disable=unused-argument

DEFAULT_APNS_ENDPOINT = "gateway.push.apple.com"


def create_notificationhubs_namespace(cmd, client,
                                      resource_group,
                                      namespace_name,
                                      sku_name,
                                      location=None,
                                      tags=None):
    body = {}
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    body.setdefault('sku', {})['name'] = sku_name  # str
    return client.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, parameters=body)


def update_notificationhubs_namespace(cmd, client,
                                      resource_group,
                                      namespace_name,
                                      location=None,
                                      tags=None,
                                      sku_name=None):
    body = client.get(resource_group_name=resource_group, namespace_name=namespace_name).as_dict()
    if tags is not None:
        body['tags'] = tags  # dictionary
    if sku_name is not None:
        body.setdefault('sku', {})['name'] = sku_name  # str
    return client.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, parameters=body)


def delete_notificationhubs_namespace(cmd, client,
                                      resource_group,
                                      namespace_name):
    return client.delete(resource_group_name=resource_group, namespace_name=namespace_name)


def get_notificationhubs_namespace(cmd, client,
                                   resource_group,
                                   namespace_name):
    return client.get(resource_group_name=resource_group, namespace_name=namespace_name)


def list_notificationhubs_namespace(cmd, client,
                                    resource_group):
    if resource_group is not None:
        return client.list(resource_group_name=resource_group)
    return client.list_all()


def check_availability_notificationhubs_namespace(cmd, client, name):
    body = {"name": name}
    return client.check_availability(parameters=body)


def list_keys_notificationhubs_namespace(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         name):
    return client.list_keys(resource_group_name=resource_group, namespace_name=namespace_name, authorization_rule_name=name)


def regenerate_keys_notificationhubs_namespace(cmd, client,
                                               resource_group,
                                               namespace_name,
                                               name,
                                               policy_key):
    return client.regenerate_keys(resource_group_name=resource_group, namespace_name=namespace_name, authorization_rule_name=name, policy_key=policy_key)


def get_authorization_rule_notificationhubs_namespace(cmd, client,
                                                      resource_group,
                                                      namespace_name,
                                                      name):
    return client.get_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, authorization_rule_name=name)


def list_authorization_rules_notificationhubs_namespace(cmd, client,
                                                        resource_group,
                                                        namespace_name):
    return client.list_authorization_rules(resource_group_name=resource_group, namespace_name=namespace_name)


def create_or_update_authorization_rule_notificationhubs_namespace(cmd, client,
                                                                   resource_group,
                                                                   namespace_name,
                                                                   name,
                                                                   rights):
    body = {}
    body['rights'] = None if rights is None else rights.split(',')
    return client.create_or_update_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, authorization_rule_name=name, properties=body)


def delete_authorization_rule_notificationhubs_namespace(cmd, client,
                                                         resource_group,
                                                         namespace_name,
                                                         name):
    return client.delete_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, authorization_rule_name=name)


def create_notificationhubs_hub(cmd, client,
                                resource_group,
                                namespace_name,
                                notification_hub_name,
                                sku_name,
                                location,
                                tags=None,
                                registration_ttl=None):
    body = {}
    body['location'] = location  # str
    body['tags'] = tags  # dictionary
    body.setdefault('sku', {})['name'] = sku_name  # str
    body['registration_ttl'] = registration_ttl  # str
    return client.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=body)


def update_notificationhubs_hub(cmd, client,
                                resource_group,
                                namespace_name,
                                notification_hub_name,
                                location=None,
                                tags=None,
                                sku_name=None):
    body = client.get(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name).as_dict()
    if tags is not None:
        body['tags'] = tags  # dictionary
    if sku_name is not None:
        body.setdefault('sku', {})['name'] = sku_name  # str
    return client.create_or_update(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=body)


def delete_notificationhubs_hub(cmd, client,
                                resource_group,
                                namespace_name,
                                notification_hub_name):
    return client.delete(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name)


def get_notificationhubs_hub(cmd, client,
                             resource_group,
                             namespace_name,
                             notification_hub_name):
    return client.get(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name)


def list_notificationhubs_hub(cmd, client,
                              resource_group,
                              namespace_name):
    return client.list(resource_group_name=resource_group, namespace_name=namespace_name)


def check_notification_hub_availability_notificationhubs_hub(cmd, client,
                                                             resource_group,
                                                             namespace_name,
                                                             notification_hub_name):
    body = {"name": notification_hub_name}
    return client.check_notification_hub_availability(resource_group_name=resource_group, namespace_name=namespace_name, parameters=body)


def regenerate_keys_notificationhubs_hub(cmd, client,
                                         resource_group,
                                         namespace_name,
                                         notification_hub_name,
                                         name,
                                         policy_key):
    return client.regenerate_keys(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, authorization_rule_name=name, policy_key=policy_key)


def get_pns_credentials_notificationhubs_hub(cmd, client,
                                             resource_group,
                                             namespace_name,
                                             notification_hub_name):
    return client.get_pns_credentials(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name)


def list_keys_notificationhubs_hub(cmd, client,
                                   resource_group,
                                   namespace_name,
                                   notification_hub_name,
                                   name):
    return client.list_keys(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, authorization_rule_name=name)


def debug_send_notificationhubs_hub(cmd, client,
                                    resource_group,
                                    namespace_name,
                                    notification_hub_name,
                                    notification_format,
                                    message=None,
                                    title='',
                                    payload=None,
                                    tag=None):

    if message is not None:
        if notification_format == 'gcm':
            parameters = {"data": {"message": message}}
        elif notification_format == 'baidu':
            parameters = {"title": title, "description": message}
        elif notification_format == 'apple':
            parameters = {"aps": {"alert": "Notification Hub test notification"}}
        elif notification_format == 'template':
            parameters = {"message": message}
        elif notification_format == 'windows':
            parameters = message
        elif notification_format == 'windowsphone':
            parameters = '''<?xml version= "1.0" encoding= "utf-8" ?>
<root>
<Value1>{}</Value1>
<Value2>{}</Value2>
</root>
'''.format(title, message)
    else:
        if notification_format not in ['windows', 'windowsphone']:
            import json
            parameters = json.loads(payload)
        else:
            parameters = payload
    print(parameters)
    custom_headers = {"servicebusnotification-format": notification_format}
    if tag is not None:
        custom_headers['servicebusnotification-tags'] = tag

    return client.debug_send(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=parameters, custom_headers=custom_headers)


def list_authorization_rules_notificationhubs_hub(cmd, client,
                                                  resource_group,
                                                  namespace_name,
                                                  notification_hub_name):
    return client.list_authorization_rules(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name)


def get_authorization_rule_notificationhubs_hub(cmd, client,
                                                resource_group,
                                                namespace_name,
                                                notification_hub_name,
                                                name):
    return client.get_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, authorization_rule_name=name)


def create_or_update_authorization_rule_notificationhubs_hub(cmd, client,
                                                             resource_group,
                                                             namespace_name,
                                                             notification_hub_name,
                                                             name,
                                                             rights):
    body = {}
    body['rights'] = None if rights is None else rights.split(',')
    return client.create_or_update_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, authorization_rule_name=name, properties=body)


def delete_authorization_rule_notificationhubs_hub(cmd, client,
                                                   resource_group,
                                                   namespace_name,
                                                   notification_hub_name,
                                                   name):
    return client.delete_authorization_rule(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, authorization_rule_name=name)


def update_gcm_credential(cmd, client,
                          resource_group,
                          namespace_name,
                          notification_hub_name,
                          google_api_key):
    body = client.get(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name).as_dict()
    body.setdefault('gcm_credential', {})['google_api_key'] = google_api_key
    return client.patch(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=body)


def update_adm_credential(cmd, client,
                          resource_group,
                          namespace_name,
                          notification_hub_name,
                          client_id,
                          client_secret):
    body = client.get(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name).as_dict()
    body.setdefault('adm_credential', {})['client_id'] = client_id
    body.setdefault('adm_credential', {})['client_secret'] = client_secret
    return client.patch(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=body)


def update_apns_credential(cmd, client,
                           resource_group,
                           namespace_name,
                           notification_hub_name,
                           apns_certificate=None,
                           certificate_key=None,
                           endpoint=DEFAULT_APNS_ENDPOINT,
                           key_id=None,
                           app_name=None,
                           app_id=None,
                           token=None):
    import base64
    body = client.get(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name).as_dict()
    if apns_certificate is not None:
        with open(apns_certificate, "rb") as f:
            data_bytes = f.read()
            cert_data = base64.b64encode(data_bytes).decode('utf-8')
            body.setdefault('apns_credential', {})['apns_certificate'] = cert_data
    if certificate_key is not None:
        body.setdefault('apns_credential', {})['certificate_key'] = certificate_key
    if endpoint is not None:
        body.setdefault('apns_credential', {})['endpoint'] = endpoint
    if key_id is not None:
        body.setdefault('apns_credential', {})['key_id'] = key_id
    if app_name is not None:
        body.setdefault('apns_credential', {})['app_name'] = app_name
    if app_id is not None:
        body.setdefault('apns_credential', {})['app_id'] = app_id
    if token is not None:
        body.setdefault('apns_credential', {})['token'] = token
    return client.patch(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=body)


def update_baidu_credential(cmd, client,
                            resource_group,
                            namespace_name,
                            notification_hub_name,
                            baidu_api_key,
                            baidu_secret_key):
    body = client.get(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name).as_dict()
    body.setdefault('baidu_credential', {})['baidu_api_key'] = baidu_api_key
    body.setdefault('baidu_credential', {})['baidu_secret_key'] = baidu_secret_key
    return client.patch(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=body)


def update_mpns_credential(cmd, client,
                           resource_group,
                           namespace_name,
                           notification_hub_name,
                           mpns_certificate,
                           certificate_key):
    body = {}
    body.setdefault('mpns_credential', {})['mpns_certificate'] = mpns_certificate
    body.setdefault('mpns_credential', {})['certificate_key'] = certificate_key
    return client.patch(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=body)


def update_wns_credential(cmd, client,
                          resource_group,
                          namespace_name,
                          notification_hub_name,
                          package_sid,
                          secret_key):
    body = client.get(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name).as_dict()
    body.setdefault('wns_credential', {})['package_sid'] = package_sid
    body.setdefault('wns_credential', {})['secret_key'] = secret_key
    return client.patch(resource_group_name=resource_group, namespace_name=namespace_name, notification_hub_name=notification_hub_name, parameters=body)
