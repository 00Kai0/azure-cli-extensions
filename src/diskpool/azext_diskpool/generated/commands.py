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


def load_command_table(self, _):

    from azext_diskpool.generated._client_factory import cf_disk_pool
    diskpool_disk_pool = CliCommandType(
        operations_tmpl='azext_diskpool.vendored_sdks.storagepool.operations._disk_pools_operations#DiskPoolsOperations'
        '.{}',
        client_factory=cf_disk_pool)
    with self.command_group('disk-pool', diskpool_disk_pool, client_factory=cf_disk_pool) as g:
        g.custom_command('list', 'disk_pool_list')
        g.custom_show_command('show', 'disk_pool_show')
        g.custom_command('create', 'disk_pool_create', supports_no_wait=True)
        g.custom_command('update', 'disk_pool_update', supports_no_wait=True)
        g.custom_command('delete', 'disk_pool_delete', supports_no_wait=True, confirmation=True)
        g.custom_command('list-outbound-network-dependency-endpoint', 'disk_pool_list_outbound_network_dependency_endpo'
                         'int')
        g.custom_command('list-skus', 'disk_pool_list_skus')
        g.custom_command('start', 'disk_pool_start', supports_no_wait=True)
        g.custom_command('stop', 'disk_pool_stop', supports_no_wait=True)
        g.custom_wait_command('wait', 'disk_pool_show')

    from azext_diskpool.generated._client_factory import cf_iscsi_target
    diskpool_iscsi_target = CliCommandType(
        operations_tmpl='azext_diskpool.vendored_sdks.storagepool.operations._iscsi_targets_operations#IscsiTargetsOper'
        'ations.{}',
        client_factory=cf_iscsi_target)
    with self.command_group('disk-pool iscsi-target', diskpool_iscsi_target, client_factory=cf_iscsi_target) as g:
        g.custom_command('list', 'disk_pool_iscsi_target_list')
        g.custom_show_command('show', 'disk_pool_iscsi_target_show')
        g.custom_command('create', 'disk_pool_iscsi_target_create', supports_no_wait=True)
        g.custom_command('update', 'disk_pool_iscsi_target_update', supports_no_wait=True)
        g.custom_command('delete', 'disk_pool_iscsi_target_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'disk_pool_iscsi_target_show')

    with self.command_group('diskpool', is_experimental=True):
        pass
