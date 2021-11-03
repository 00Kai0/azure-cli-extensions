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

from knack.help_files import helps


helps['network manager'] = """
    type: group
    short-summary: Manage networkmanager with network
"""

helps['network manager list'] = """
    type: command
    short-summary: "List network managers in a resource group."
    examples:
      - name: List Azure Virtual Network Manager
        text: |-
               az network manager list --resource-group "rg1"
"""

helps['network manager show'] = """
    type: command
    short-summary: "Gets the specified Network Manager."
    examples:
      - name: Get Azure Virtual Network Manager
        text: |-
               az network manager show --name "testNetworkManager" --resource-group "rg1"
"""

helps['network manager create'] = """
    type: command
    short-summary: "Create a Network Manager."
    parameters:
      - name: --network-manager-scopes
        short-summary: "Scope of Network Manager."
        long-summary: |
            Usage: --network-manager-scopes management-groups=XX subscriptions=XX

            management-groups: List of management groups.
            subscriptions: List of subscriptions.
    examples:
      - name: Create/Update Azure Virtual Network Manager
        text: |-
               az network manager create --name "TestNetworkManager" --description "My Test Network Manager" \
--display-name "TestNetworkManager" --scope-accesses "SecurityAdmin" "Connectivity" \
--network-manager-scopes management-groups="/providers/Microsoft.Management/testmg" subscriptions="/subscriptions/00000000-0000-0\
000-0000-000000000000" --resource-group "rg1"
"""

helps['network manager update'] = """
    type: command
    short-summary: "Update a Network Manager."
    parameters:
      - name: --network-manager-scopes
        short-summary: "Scope of Network Manager."
        long-summary: |
            Usage: --network-manager-scopes management-groups=XX subscriptions=XX

            management-groups: List of management groups.
            subscriptions: List of subscriptions.
"""

helps['network manager delete'] = """
    type: command
    short-summary: "Deletes a network manager."
    examples:
      - name: Delete Azure Virtual Network Manager
        text: |-
               az network manager delete --name "testNetworkManager" --resource-group "rg1"
"""

helps['network manager post-commit'] = """
    type: command
    short-summary: "Post a Network Manager Commit."
    examples:
      - name: Post Azure Virtual Network Manager Commit
        text: |-
               az network manager post-commit --network-manager-name "testNetworkManager" --commit-type "SecurityAdmin" \
--configuration-ids "/subscriptions/subscriptionC/resourceGroups/resoureGroupSample/providers/Microsoft.Network/network\
Managers/testNetworkManager/securityConfigurations/SampleSecurityConfig" --target-locations "eastus" --resource-group \
"resoureGroupSample"
"""

helps['network manager list-deploy-status'] = """
    type: command
    short-summary: "Post List of Network Manager Deployment Status."
    examples:
      - name: Post Azure Virtual Network Manager Deployment Status
        text: |-
               az network manager list-deploy-status --network-manager-name "testNetworkManager" --deployment-types \
"Connectivity" "SecurityAdmin" --regions "eastus" "westus" --resource-group "resoureGroupSample"
"""

helps['network manager list-effect-vnet'] = """
    type: command
    short-summary: "List effective virtual networks in a network manager."
    examples:
      - name: List Effective Virtual Networks List By Network Groups
        text: |-
               az network manager list-effect-vnet --network-manager-name "testNetworkManager" \
--conditional-members "location=\'useast2\'" --resource-group "rg1"
"""

helps['network manager list-active-connectivity-config'] = """
    type: command
    short-summary: "Lists active configurations in a network manager."
    examples:
      - name: Get Azure Virtual Network Manager Active Configuration
        text: |-
               az network manager list-active-connectivity-config --network-manager-name "testNetworkManager" --resource-group \
"myResourceGroup"
"""

helps['network manager list-effective-connectivity-config'] = """
    type: command
    short-summary: "Lists effective configuration in a network manager."
    examples:
      - name: Get Azure Virtual Network Manager Effective Configuration
        text: |-
               az network manager list-effective-connectivity-config --virtual-network-name "myVirtualNetwork" --resource-group "myResourceGroup"
"""

helps['network manager list-effective-security-admin-rule'] = """
    type: command
    short-summary: "Lists effective configuration in a network manager."
    examples:
      - name: Get Azure Virtual Network Manager Effective Configuration
        text: |-
               az network manager list-effective-security-admin-rule --virtual-network-name "myVirtualNetwork" --resource-group "myResourceGroup"
"""

helps['network manager list-active-security-admin-rule'] = """
    type: command
    short-summary: "Lists active security admin rule in a network manager."
    examples:
      - name: Get Azure Virtual Network Manager Active Security Admin Rule
        text: |-
               az network manager list-active-security-admin-rule --network-manager-name "testNetworkManager" --resource-group \
"myResourceGroup" --region "eastus2euap"
"""

helps['network manager list-active-security-user-rule'] = """
    type: command
    short-summary: "Lists active security user rule in a network manager."
    examples:
      - name: Get Azure Virtual Network Manager Active Security User Rule
        text: |-
               az network manager list-active-security-user-rule --network-manager-name "testNetworkManager" --resource-group \
"myResourceGroup --region eastus2euap"
"""

helps['network manager connect-config'] = """
    type: group
    short-summary: Manage connectivityconfiguration with network
"""

helps['network manager connect-config list'] = """
    type: command
    short-summary: "Lists all the network manager connectivity configuration in a specified network manager."
    examples:
      - name: Get Azure Virtual Network Manager Connecitivity Configuration List
        text: |-
               az network manager connect-config list --network-manager-name "testNetworkManager" --resource-group \
"myResourceGroup"
"""

helps['network manager connect-config show'] = """
    type: command
    short-summary: "Gets a Network Connectivity Configuration, specified by the resource group, network manager name, \
and connectivity Configuration name."
    examples:
      - name: Get Azure Virtual Network Manager Connectivity Configuration
        text: |-
               az network manager connect-config show --configuration-name "myTestConnectivityConfig" \
--network-manager-name "testNetworkManager" --resource-group "myResourceGroup"
"""

helps['network manager connect-config create'] = """
    type: command
    short-summary: "Create a new network manager connectivity configuration."
    parameters:
      - name: --applies-to-groups
        short-summary: "Groups for configuration"
        long-summary: |
            Usage: --applies-to-groups network-group-id=XX use-hub-gateway=XX is-global=XX group-connectivity=XX

            network-group-id: Network group Id.
            use-hub-gateway: Flag if need to use hub gateway.
            is-global: Flag if global is supported.
            group-connectivity: Group connectivity type. Allowed values: None, DirectlyConnected

            Multiple actions can be specified by using more than one --applies-to-groups argument.
      - name: --hubs
        short-summary: "The hub vnets"
        long-summary: |
            Usage: --hubs resource-id=XX resource-type=XX

            resource-id: Resource ID
            resource-type: Resource Type

            Multiple actions can be specified by using more than one --hubs argument.
    examples:
      - name: Create/Update Azure Virtual Network Manager Connectivity Configuration
        text: |-
               az network manager connect-config create --configuration-name "myTestConnectivityConfig" --description \
"Sample Configuration" --applies-to-groups group-connectivity="None" is-global=false \
network-group-id="subscriptions/subscriptionA/resourceGroups/myResourceGroup/providers/Microsoft.Network/networkManager\
s/testNetworkManager/networkManagerGroups/group1" use-hub-gateway=true --connectivity-topology "HubAndSpoke" \
--delete-existing-peering true --display-name "myTestConnectivityConfig" --hubs resource-id="subscriptions/subscriptionA/resource\
Groups/myResourceGroup/providers/Microsoft.Network/virtualNetworks/myTestConnectivityConfig" resource-type="Microsoft.Network/virtualNetworks" \
--is-global true --network-manager-name "testNetworkManager" --resource-group "myResourceGroup"
"""

helps['network manager connect-config update'] = """
    type: command
    short-summary: "Update a new network manager connectivity configuration."
    parameters:
      - name: --applies-to-groups
        short-summary: "Groups for configuration"
        long-summary: |
            Usage: --applies-to-groups network-group-id=XX use-hub-gateway=XX is-global=XX group-connectivity=XX

            network-group-id: Network group Id.
            use-hub-gateway: Flag if need to use hub gateway.
            is-global: Flag if global is supported.
            group-connectivity: Group connectivity type. Allowed values: None, DirectlyConnected

            Multiple actions can be specified by using more than one --applies-to-groups argument.
      - name: --hubs
        short-summary: "The hub vnets"
        long-summary: |
            Usage: --hubs resource-id=XX resource-type=XX

            resource-id: Resource ID
            resource-type: Resource Type

            Multiple actions can be specified by using more than one --hubs argument.
"""

helps['network manager connect-config delete'] = """
    type: command
    short-summary: "Deletes a network manager connectivity configuration, specified by the resource group, network \
manager name, and connectivity configuration name."
    examples:
      - name: Get Azure Virtual Network Manager Connectivity Configuration
        text: |-
               az network manager connect-config delete --configuration-name "myTestConnectivityConfig" \
--network-manager-name "testNetworkManager" --resource-group "myResourceGroup"
"""

helps['network manager group'] = """
    type: group
    short-summary: Manage networkgroup with network
"""

helps['network manager group list'] = """
    type: command
    short-summary: "Lists the specified network group."
    examples:
      - name: List Azure Virtual Network Manager Network Groups
        text: |-
               az network manager group list --network-manager-name "testNetworkManager" --resource-group "rg1"
"""

helps['network manager group show'] = """
    type: command
    short-summary: "Gets the specified network group."
    examples:
      - name: Get Azure Virtual Network Manager Network Group
        text: |-
               az network manager group show --name "TestNetworkGroup" --network-manager-name "testNetworkManager" \
--resource-group "rg1"
"""

helps['network manager group create'] = """
    type: command
    short-summary: "Create a network group."
    parameters:
      - name: --group-members
        short-summary: "Group members of network group."
        long-summary: |
            Usage: --group-members resource-id=XX

            resource-id: Resource Id.

            Multiple actions can be specified by using more than one --group-members argument.
    examples:
      - name: Create/Update Azure Virtual Network Manager Network Group
        text: |-
               az network manager group create --name "TestNetworkGroup" --network-manager-name "testNetworkManager" \
--description "A sample group" --conditional-membership "" --display-name "My Network Group" --group-members \
resource-id="/subscriptions/subscriptionC/resourceGroup/rg1/providers/Microsoft.Network/virtualnetworks/vnet1" \
--member-type "Microsoft.Network/virtualNetworks" --resource-group "rg1"
"""

helps['network manager group update'] = """
    type: command
    short-summary: "Update a network group."
    parameters:
      - name: --group-members
        short-summary: "Group members of network group."
        long-summary: |
            Usage: --group-members resource-id=XX

            resource-id: Resource Id.

            Multiple actions can be specified by using more than one --group-members argument.
"""

helps['network manager group delete'] = """
    type: command
    short-summary: "Deletes a network group."
    examples:
      - name: Delete Azure Virtual Network Manager Group
        text: |-
               az network manager group delete --name "TestNetworkGroup" --network-manager-name "testNetworkManager" \
--resource-group "rg1"
"""

helps['network manager group list-effect-vnet'] = """
    type: command
    short-summary: "Lists all effective virtual networks by specified network group."
    examples:
      - name: List Effective Virtual Networks List By Network Groups
        text: |-
               az network manager group list-effect-vnet --network-group-name "TestNetworkGroup" \
--network-manager-name "testNetworkManager" --resource-group "rg1"
"""

helps['network manager security-user-config'] = """
    type: group
    short-summary: Manage securityuserconfiguration with network
"""

helps['network manager security-user-config list'] = """
    type: command
    short-summary: "Lists all the network manager security user configurations in a network manager, in a paginated \
format."
    examples:
      - name: List security user configurations in a network manager
        text: |-
               az network manager security-user-config list --network-manager-name "testNetworkManager" --resource-group \
"rg1"
"""

helps['network manager security-user-config show'] = """
    type: command
    short-summary: "Retrieves a network manager security user Configuration."
    examples:
      - name: Get security user configurations
        text: |-
               az network manager security-user-config show --configuration-name "myTestSecurityConfig" \
--network-manager-name "testNetworkManager" --resource-group "rg1"
"""

helps['network manager security-user-config create'] = """
    type: command
    short-summary: "Create a network manager security user Configuration."
    examples:
      - name: Create network manager security user Configuration
        text: |-
               az network manager security-user-config create --configuration-name "myTestSecurityConfig" \
--network-manager-name "testNetworkManager" --resource-group "rg1" --description "A sample policy" \
--delete-existing-ns-gs true --security-type "UserPolicy"
"""

helps['network manager security-user-config update'] = """
    type: command
    short-summary: "Update a network manager security user Configuration."
"""

helps['network manager security-user-config delete'] = """
    type: command
    short-summary: "Deletes a network manager security user Configuration."
    examples:
      - name: Delete network manager security user Configuration
        text: |-
               az network manager security-user-config delete --configuration-name "myTestSecurityConfig" \
--network-manager-name "testNetworkManager" --resource-group "rg1"
"""

helps['network manager security-admin-config'] = """
    type: group
    short-summary: Manage securityadminconfiguration with network
"""

helps['network manager security-admin-config list'] = """
    type: command
    short-summary: "Lists all the network manager security admin configurations in a network manager, in a paginated \
format."
    examples:
      - name: List security admin configurations in a network manager
        text: |-
               az network manager security-admin-config list --network-manager-name "testNetworkManager" --resource-group \
"rg1"
"""

helps['network manager security-admin-config show'] = """
    type: command
    short-summary: "Retrieves a network manager security admin Configuration."
    examples:
      - name: Get security admin configurations
        text: |-
               az network manager security-admin-config show --configuration-name "myTestSecurityConfig" \
--network-manager-name "testNetworkManager" --resource-group "rg1"
"""

helps['network manager security-admin-config create'] = """
    type: command
    short-summary: "Create a network manager security admin Configuration."
    examples:
      - name: Create network manager security admin Configuration
        text: |-
               az network manager security-admin-config create --configuration-name "myTestSecurityConfig" \
--network-manager-name "testNetworkManager" --resource-group "rg1" --description "A sample policy" \
--delete-existing-ns-gs true --security-type "AdminPolicy"
"""

helps['network manager security-admin-config update'] = """
    type: command
    short-summary: "Update a network manager security admin Configuration."
"""

helps['network manager security-admin-config delete'] = """
    type: command
    short-summary: "Deletes a network manager security admin Configuration."
    examples:
      - name: Delete network manager security admin Configuration
        text: |-
               az network manager security-admin-config delete --configuration-name "myTestSecurityConfig" \
--network-manager-name "testNetworkManager" --resource-group "rg1"
"""

helps['network manager security-admin-config rule-collection'] = """
    type: group
    short-summary: Manage admin rule collection with network
"""

helps['network manager security-admin-config rule-collection create'] = """
    type: command
    short-summary: "Create a network manager security configuration admin rule collection."
    examples:
      - name: Create security admin rule collections
        text: |-
               az network manager security-admin-config rule-collection create --configuration-name "myTestSecurityConfig" --network-manager-name "testNetworkManager"  -g "rg1" \
--rule-collection-name "myTestCollection" --description "A sample description" --display-name "ASampleCollection" \
--applies-to-groups  network-group-id="sub_id/resourceGroups/rgid/providers/Microsoft.Network/networkManagers/TestNetworkManager/networkGroups/TestNetworkGroup"
"""

helps['network manager security-admin-config rule-collection list'] = """
    type: command
    short-summary: "List network manager security configuration admin rule collections."
    examples:
      - name: List security admin rule collections
        text: |-
               az network manager security-admin-config rule-collection list --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1"
"""

helps['network manager security-admin-config rule-collection update'] = """
    type: command
    short-summary: "Update a network manager security configuration admin rule collection in a subscription."
    examples:
      - name: Update security admin rule collection
        text: |-
               az network manager security-admin-config rule-collection update --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection" --display-name "ASampleCollection2"
"""

helps['network manager security-admin-config rule-collection show'] = """
    type: command
    short-summary: "Gets a network manager security configuration admin rule collection in a subscription."
    examples:
      - name: Gets security admin rule collection
        text: |-
               az network manager security-admin-config rule-collection show --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection"
"""

helps['network manager security-admin-config rule-collection delete'] = """
    type: command
    short-summary: "Delete an admin rule collection."
    examples:
      - name: Delete an admin rule collection.
        text: |-
               az network manager security-admin-config rule-collection delete --configuration-name "myTestSecurityConfig" --network-manager-name "testNetworkManager" \
--resource-group "rg1" --rule-collection-name "myTestCollection"
"""


helps['network manager security-admin-config rule-collection rule'] = """
    type: group
    short-summary: Manage adminrule with network
"""

helps['network manager security-admin-config rule-collection rule create'] = """
    type: command
    short-summary: "Create a network manager security configuration admin rule."
    parameters:
      - name: --sources
        short-summary: "The CIDR or source IP ranges."
        long-summary: |
            Usage: --sources address-prefix=XX address-prefix-type=XX

            address-prefix: Address prefix.
            address-prefix-type: Address prefix type.

            Multiple actions can be specified by using more than one --sources argument.
      - name: --destinations
        short-summary: "The destination address prefixes. CIDR or destination IP ranges."
        long-summary: |
            Usage: --destination address-prefix=XX address-prefix-type=XX

            address-prefix: Address prefix.
            address-prefix-type: Address prefix type.

            Multiple actions can be specified by using more than one --destination argument.
    examples:
      - name: Create security admin rules
        text: |-
               az network manager security-admin-config rule-collection rule create --configuration-name "myTestSecurityConfig" --network-manager-name "testNetworkManager" \
--resource-group "rg1" --rule-collection-name "myTestCollection" --rule-name "SampleAdminRule" \
--kind "Custom" --protocol "Tcp" --access "Allow" --priority 32 --direction "Inbound"
"""

helps['network manager security-admin-config rule-collection rule list'] = """
    type: command
    short-summary: "Retrieves a network manager security configuration admin rule."
    examples:
      - name: List security admin rules
        text: |-
               az network manager security-admin-config rule-collection rule list --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection"
"""

helps['network manager security-admin-config rule-collection rule update'] = """
    type: command
    short-summary: "Update a network manager security configuration admin rule in a subscription."
    parameters:
      - name: --sources
        short-summary: "The CIDR or source IP ranges."
        long-summary: |
            Usage: --sources address-prefix=XX address-prefix-type=XX

            address-prefix: Address prefix.
            address-prefix-type: Address prefix type.

            Multiple actions can be specified by using more than one --sources argument.
      - name: --destinations
        short-summary: "The destination address prefixes. CIDR or destination IP ranges."
        long-summary: |
            Usage: --destination address-prefix=XX address-prefix-type=XX

            address-prefix: Address prefix.
            address-prefix-type: Address prefix type.

            Multiple actions can be specified by using more than one --destination argument.
    examples:
      - name: Update security admin rule
        text: |-
               az network manager security-admin-config rule-collection rule update --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection" --rule-name "SampleAdminRule" --access "Deny"
"""

helps['network manager security-admin-config rule-collection rule show'] = """
    type: command
    short-summary: "Gets a network manager security configuration admin rule in a subscription."
    examples:
      - name: Gets security admin rule
        text: |-
               az network manager security-admin-config rule-collection rule show --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection" --rule-name "SampleAdminRule"
"""

helps['network manager security-admin-config rule-collection rule delete'] = """
    type: command
    short-summary: "Deletes an admin rule."
    examples:
      - name: Deletes an admin rule.
        text: |-
               az network manager security-admin-config rule-collection rule delete --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection" --rule-name "SampleAdminRule"
"""

helps['network manager security-user-config rule-collection'] = """
    type: group
    short-summary: Manage user rule collection with network
"""

helps['network manager security-user-config rule-collection create'] = """
    type: command
    short-summary: "Create a network manager security configuration user rule collection."
    examples:
      - name: Create security user rule collections
        text: |-
               az network manager security-user-config rule-collection create --configuration-name "myTestSecurityConfig" --network-manager-name "testNetworkManager"  -g "rg1" \
--rule-collection-name myTestCollection --description "A sample description" --display-name "ASampleCollection" \
--applies-to-groups  network-group-id=sub_id/resourceGroups/rgid/providers/Microsoft.Network/networkManagers/TestNetworkManager/networkGroups/TestNetworkGroup
"""

helps['network manager security-user-config rule-collection list'] = """
    type: command
    short-summary: "List network manager security configuration user rule collections."
    examples:
      - name: List security user rule collections
        text: |-
               az network manager security-user-config rule-collection list --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1"
"""

helps['network manager security-user-config rule-collection update'] = """
    type: command
    short-summary: "Update a network manager security configuration user rule collection in a subscription."
    examples:
      - name: Update security user rule collection
        text: |-
               az network manager security-user-config rule-collection update --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection" --display-name "ASampleCollection2"
"""

helps['network manager security-user-config rule-collection show'] = """
    type: command
    short-summary: "Gets a network manager security configuration user rule collection in a subscription."
    examples:
      - name: Gets security user rule collection
        text: |-
               az network manager security-user-config rule-collection show --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection"
"""

helps['network manager security-user-config rule-collection delete'] = """
    type: command
    short-summary: "Delete an user rule collection."
    examples:
      - name: Delete an user rule collection.
        text: |-
               az network manager security-user-config rule-collection delete --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection"
"""

helps['network manager security-user-config rule-collection rule'] = """
    type: group
    short-summary: Manage userrule with network
"""

helps['network manager security-user-config rule-collection rule list'] = """
    type: command
    short-summary: "Lists all user rules in a security configuration."
    examples:
      - name: List security user rules
        text: |-
               az network manager security-user-config rule-collection rule list --configuration-name "myTestConnectivityConfig" \
--network-manager-name "testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection"
"""

helps['network manager security-user-config rule-collection rule show'] = """
    type: command
    short-summary: "Gets a user rule."
    examples:
      - name: Gets a user rule
        text: |-
               az network manager security-user-config rule-collection rule show --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-name "SampleUserRule" --rule-collection-name "myTestCollection"
"""

helps['network manager security-user-config rule-collection rule create'] = """
    type: command
    short-summary: "Create a user rule."
    parameters:
      - name: --sources
        short-summary: "The CIDR or source IP ranges."
        long-summary: |
            Usage: --sources address-prefix=XX address-prefix-type=XX

            address-prefix: Address prefix.
            address-prefix-type: Address prefix type.

            Multiple actions can be specified by using more than one --sources argument.
      - name: --destinations
        short-summary: "The destination address prefixes. CIDR or destination IP ranges."
        long-summary: |
            Usage: --destination address-prefix=XX address-prefix-type=XX

            address-prefix: Address prefix.
            address-prefix-type: Address prefix type.

            Multiple actions can be specified by using more than one --destination argument.
    examples:
      - name: Create a user rule
        text: |-
               az network manager security-user-config rule-collection rule create --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection" --rule-name "SampleUserRule" --description "Sample User Rule" \
--destinations address-prefix="*" address-prefix-type="IPPrefix" --dest-port-ranges 22 --direction "Inbound" \
--sources address-prefix="*" address-prefix-type="IPPrefix" --source-port-ranges "0-65535" --protocol "Tcp"
"""

helps['network manager security-user-config rule-collection rule update'] = """
    type: command
    short-summary: "Update a user rule."
    parameters:
      - name: --sources
        short-summary: "The CIDR or source IP ranges."
        long-summary: |
            Usage: --sources address-prefix=XX address-prefix-type=XX

            address-prefix: Address prefix.
            address-prefix-type: Address prefix type.

            Multiple actions can be specified by using more than one --sources argument.
      - name: --destinations
        short-summary: "The destination address prefixes. CIDR or destination IP ranges."
        long-summary: |
            Usage: --destination address-prefix=XX address-prefix-type=XX

            address-prefix: Address prefix.
            address-prefix-type: Address prefix type.

            Multiple actions can be specified by using more than one --destination argument.
    examples:
      - name: Update a user rule
        text: |-
               az network manager security-user-config rule-collection rule update --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection" --rule-name "SampleUserRule" --description "Sample User Rule"
"""

helps['network manager security-user-config rule-collection rule delete'] = """
    type: command
    short-summary: "Deletes a user rule."
    examples:
      - name: Delete a user rule.
        text: |-
               az network manager security-user-config rule-collection rule delete --configuration-name "myTestSecurityConfig" --network-manager-name \
"testNetworkManager" --resource-group "rg1" --rule-collection-name "myTestCollection" --rule-name "SampleUserRule"
"""
