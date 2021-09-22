# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long

import os
import unittest

from azure.cli.testsdk import ScenarioTest
from azure.cli.testsdk import ResourceGroupPreparer

from .preparers import VirtualNetworkPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


# Test class for Scenario
class NetworkScenarioTest(ScenarioTest):

    def __init__(self, *args, **kwargs):
        super(NetworkScenarioTest, self).__init__(*args, **kwargs)

    @ResourceGroupPreparer(name_prefix='test_network_manager', location='jioindiawest')
    def test_network_manager_crud(self, resource_group):
        self.kwargs.update({
            'name': 'TestNetworkManager',
            'description': '"My Test Network Manager"',
            'display_name': 'TestNetworkManager',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id())
        })

        self.cmd('network manager create --name {name} --description {description} --display-name {display_name} '
                 '--network-manager-scope-accesses "Routing" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l jioindiawest '
                 '--resource-group {rg}')

        # Update is not allowed for NM.
        # self.cmd('network manager update --resource-group {rg} --name {name} --tags key1=value1')

        self.cmd('network manager list --resource-group {rg}')

        self.cmd('network manager delete --resource-group {rg} --name {name} --yes')

    @ResourceGroupPreparer(name_prefix='test_network_manager_group', location='jioindiawest')
    @VirtualNetworkPreparer()
    def test_network_manager_group_crud(self, virtual_network, resource_group):

        self.kwargs.update({
            'name': 'TestNetworkGroup',
            'manager_name': 'TestNetworkManager',
            'description': '"A sample group"',
            'display_name': 'MyNetworkGroup',
            'member_type': 'VirtualNetwork',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
            'virtual_network': virtual_network
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--network-manager-scope-accesses "Routing" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l jioindiawest '
                 '--resource-group {rg}')

        self.cmd('network manager group create --name {name} --network-manager-name {manager_name} --description {description} '
                 '--conditional-membership "" --display-name {display_name} --member-type {member_type}  -g {rg} '
                 '--group-members vnet-id="{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualnetworks/{virtual_network}" '
                 'subnet-id=""')

        self.cmd('network manager group update -g {rg} --name {name} --network-manager-name {manager_name} --description "Desc changed."')
        self.cmd('network manager group show -g {rg} --name {name} --network-manager-name {manager_name}')
        self.cmd('network manager group list -g {rg} --network-manager-name {manager_name}')
        self.cmd('network manager group delete -g {rg} --name {name} --network-manager-name {manager_name} --yes')

    @ResourceGroupPreparer(name_prefix='test_network_manager_security_user_config', location='jioindiawest')
    def test_network_manager_security_user_config_crud(self, resource_group):

        self.kwargs.update({
            'name': 'myTestSecurityConfig',
            'manager_name': 'TestNetworkManager',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--network-manager-scope-accesses "SecurityUser" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l jioindiawest '
                 '--resource-group {rg}')

        self.cmd('network manager security-user-config create --configuration-name {name} --network-manager-name {manager_name} -g {rg} '
                 '--description {description} --delete-existing-ns-gs true --security-type "UserPolicy" --display-name MyTestConfig')

        self.cmd('network manager security-user-config update --configuration-name {name} --network-manager-name {manager_name} -g {rg} '
                 '--description "test_description"')
        self.cmd('network manager security-user-config list --network-manager-name {manager_name} -g {rg}')
        self.cmd('network manager security-user-config show --configuration-name {name} --network-manager-name {manager_name} -g {rg}')
        self.cmd('network manager security-user-config delete --configuration-name {name} --network-manager-name {manager_name} -g {rg} --yes')

    @ResourceGroupPreparer(name_prefix='test_network_manager_security_admin_config', location='jioindiawest')
    def test_network_manager_security_admin_config_crud(self, resource_group):

        self.kwargs.update({
            'name': 'myTestSecurityConfig',
            'manager_name': 'TestNetworkManager',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--network-manager-scope-accesses "SecurityAdmin" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l jioindiawest '
                 '--resource-group {rg}')

        self.cmd('network manager security-admin-config create --configuration-name {name} --network-manager-name {manager_name} -g {rg} '
                 '--description {description} --delete-existing-ns-gs true --security-type "AdminPolicy" --display-name MyTestConfig')

        self.cmd('network manager security-admin-config update --configuration-name {name} --network-manager-name {manager_name} -g {rg} '
                 '--description "test_description"')
        self.cmd('network manager security-admin-config list --network-manager-name {manager_name} -g {rg}')
        self.cmd('network manager security-admin-config show --configuration-name {name} --network-manager-name {manager_name} -g {rg}')

        # test nm commit
        # self.cmd('network manager commit post --network-manager-name {manager_name} --commit-type "SecurityAdmin" --target-locations "eastus2" -g {rg} '
        #          '--configuration-ids {sub}/resourceGroups/{rg}/providers/Microsoft.Network/networkManagers/{manager_name}/securityAdminConfigurations/{name}')

        # test nm uncommit
        # self.cmd('network manager commit post --network-manager-name {manager_name} --commit-type "SecurityAdmin" --target-locations "eastus2" -g {rg} ')

        self.cmd('network manager security-admin-config delete --configuration-name {name} --network-manager-name {manager_name} -g {rg} --yes')


    @ResourceGroupPreparer(name_prefix='test_network_manager_security_admin_rule_collection_crud', location='jioindiawest')
    @VirtualNetworkPreparer()
    def test_network_manager_security_admin_rule_collection_crud(self, virtual_network, resource_group):

        self.kwargs.update({
            'collection_name': '',
            'config_name': 'myTestSecurityConfig',
            'manager_name': 'TestNetworkManager',
            'group_name': 'TestNetworkGroup',
            'description': '"A sample policy"',
            'sub': '/subscriptions/{}'.format(self.get_subscription_id()),
        })

        self.cmd('network manager create --name {manager_name} --description "My Test Network Manager" --display-name "TestNetworkManager" '
                 '--network-manager-scope-accesses "SecurityAdmin" "Connectivity" '
                 '--network-manager-scopes '
                 ' subscriptions={sub} '
                 '-l jioindiawest '
                 '--resource-group {rg}')

        self.cmd('network manager group create --name {group_name} --network-manager-name {manager_name} --description {description} '
                 '--conditional-membership "" --display-name ASampleGroup --member-type VirtualNetwork  -g {rg} '
                 '--group-members vnet-id="{sub}/resourceGroups/{rg}/providers/Microsoft.Network/virtualnetworks/{virtual_network}" '
                 'subnet-id=""')

        self.cmd('network manager security-admin-config create --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} '
                 '--description {description} --delete-existing-ns-gs true --security-type "AdminPolicy" --display-name MyTestConfig')

        self.cmd('network manager admin-rule collection --configuration-name {config_name} --network-manager-name {manager_name} -g {rg} '
                 '--role-collection-name {collection_name} --description {description} --display-name ASampleCollection '
                 '--applies-to-groups  network-group-id={sub}/resourceGroups/{rg}/providers/Microsoft.Network/networkManagers/{manager_name}/networkGroups/{group_name}')

