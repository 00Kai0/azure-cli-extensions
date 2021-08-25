# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddNetworkManagerScopes(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.network_manager_scopes = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'management-groups':
                d['management_groups'] = v
            elif kl == 'subscriptions':
                d['subscriptions'] = v
            else:
                raise CLIError('Unsupported Key {} is provided for parameter network_manager_scopes. All possible keys '
                               'are: management-groups, subscriptions'.format(k))
        return d


class AddConnectivityconfigurationsAppliesToGroups(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddConnectivityconfigurationsAppliesToGroups, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'network-group-id':
                d['network_group_id'] = v[0]
            elif kl == 'use-hub-gateway':
                d['use_hub_gateway'] = v[0]
            elif kl == 'is-global':
                d['is_global'] = v[0]
            elif kl == 'group-connectivity':
                d['group_connectivity'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter applies_to_groups. All possible keys are: '
                               'network-group-id, use-hub-gateway, is-global, group-connectivity'.format(k))
        return d


class AddGroupMembers(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddGroupMembers, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'resource-id':
                d['resource_id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter group_members. All possible keys are: '
                               'resource-id'.format(k))
        return d


class AddSecurityconfigurationsAppliesToGroups(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddSecurityconfigurationsAppliesToGroups, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'network-group-id':
                d['network_group_id'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter applies_to_groups. All possible keys are: '
                               'network-group-id'.format(k))
        return d


class AddNetworkSecurityGroupImports(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddNetworkSecurityGroupImports, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'network-security-group-uri':
                d['network_security_group_uri'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter network_security_group_imports. All '
                               'possible keys are: network-security-group-uri'.format(k))
        return d


class AddSource(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddSource, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'address-prefix':
                d['address_prefix'] = v[0]
            elif kl == 'address-prefix-type':
                d['address_prefix_type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter source. All possible keys are: '
                               'address-prefix, address-prefix-type'.format(k))
        return d


class AddDestination(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDestination, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'address-prefix':
                d['address_prefix'] = v[0]
            elif kl == 'address-prefix-type':
                d['address_prefix_type'] = v[0]
            else:
                raise CLIError('Unsupported Key {} is provided for parameter destination. All possible keys are: '
                               'address-prefix, address-prefix-type'.format(k))
        return d