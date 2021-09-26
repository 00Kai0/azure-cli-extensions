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


helps['elastic'] = '''
    type: group
    short-summary: Manage Microsoft Elastic
'''

helps['elastic monitor'] = """
    type: group
    short-summary: Manage monitor with elastic
"""

helps['elastic monitor list'] = """
    type: command
    short-summary: "List all monitors under the specified resource group. And List all monitors under the specified \
subscription."
    examples:
      - name: Monitors_ListByResourceGroup
        text: |-
               az elastic monitor list --resource-group "myResourceGroup"
      - name: Monitors_List
        text: |-
               az elastic monitor list
"""

helps['elastic monitor show'] = """
    type: command
    short-summary: "Get the properties of a specific monitor resource."
    examples:
      - name: Monitors_Get
        text: |-
               az elastic monitor show --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['elastic monitor create'] = """
    type: command
    short-summary: "Create a monitor resource."
    examples:
      - name: Monitors_Create
        text: |-
               az elastic monitor create --monitor-name "myMonitor" --location "West US 2" --user-info \
"{\\"companyInfo\\":{\\"business\\":\\"Technology\\",\\"country\\":\\"US\\",\\"domain\\":\\"microsoft.com\\",\\"employe\
eNumber\\":\\"10000\\",\\"state\\":\\"WA\\"},\\"companyName\\":\\"Microsoft\\",\\"emailAddress\\":\\"alice@microsoft.co\
m\\",\\"firstName\\":\\"Alice\\",\\"lastName\\":\\"Bob\\"}" --name "free_Monthly" --tags Environment="Dev" \
--resource-group "myResourceGroup"
"""

helps['elastic monitor update'] = """
    type: command
    short-summary: "Update a monitor resource."
    examples:
      - name: Monitors_Update
        text: |-
               az elastic monitor update --name "myMonitor" --tags Environment="Dev" --resource-group \
"myResourceGroup"
"""

helps['elastic monitor delete'] = """
    type: command
    short-summary: "Delete a monitor resource."
    examples:
      - name: Monitors_Delete
        text: |-
               az elastic monitor delete --name "myMonitor" --resource-group "myResourceGroup"
"""

helps['elastic monitor wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the elastic monitor is met.
    examples:
      - name: Pause executing next line of CLI script until the elastic monitor is successfully created.
        text: |-
               az elastic monitor wait --name "myMonitor" --resource-group "myResourceGroup" --created
      - name: Pause executing next line of CLI script until the elastic monitor is successfully deleted.
        text: |-
               az elastic monitor wait --name "myMonitor" --resource-group "myResourceGroup" --deleted
"""

helps['elastic monitored-resource'] = """
    type: group
    short-summary: Manage monitored resource with elastic
"""

helps['elastic monitored-resource list'] = """
    type: command
    short-summary: "List the resources currently being monitored by the Elastic monitor resource."
    examples:
      - name: MonitoredResources_List
        text: |-
               az elastic monitored-resource list --monitor-name "myMonitor" --resource-group "myResourceGroup"
"""

helps['elastic deployment-info'] = """
    type: group
    short-summary: Manage deployment info with elastic
"""

helps['elastic deployment-info list'] = """
    type: command
    short-summary: "Fetch information regarding Elastic cloud deployment corresponding to the Elastic monitor \
resource."
    examples:
      - name: DeploymentInfo_List
        text: |-
               az elastic deployment-info list --monitor-name "myMonitor" --resource-group "myResourceGroup"
"""

helps['elastic tag-rule'] = """
    type: group
    short-summary: Manage tag rule with elastic
"""

helps['elastic tag-rule list'] = """
    type: command
    short-summary: "List the tag rules for a given monitor resource."
    examples:
      - name: TagRules_List
        text: |-
               az elastic tag-rule list --monitor-name "myMonitor" --resource-group "myResourceGroup"
"""

helps['elastic tag-rule show'] = """
    type: command
    short-summary: "Get a tag rule set for a given monitor resource."
    examples:
      - name: TagRules_Get
        text: |-
               az elastic tag-rule show --monitor-name "myMonitor" --resource-group "myResourceGroup" --rule-set-name \
"default"
"""

helps['elastic tag-rule create'] = """
    type: command
    short-summary: "Create a tag rule set for a given monitor resource."
    parameters:
      - name: --filtering-tags
        short-summary: "List of filtering tags to be used for capturing logs. This only takes effect if \
SendActivityLogs flag is enabled. If empty, all resources will be captured. If only Exclude action is specified, the \
rules will apply to the list of all available resources. If Include actions are specified, the rules will only include \
resources with the associated tags."
        long-summary: |
            Usage: --filtering-tags name=XX value=XX action=XX

            name: The name (also known as the key) of the tag.
            value: The value of the tag.
            action: Valid actions for a filtering tag.

            Multiple actions can be specified by using more than one --filtering-tags argument.
    examples:
      - name: TagRules_CreateOrUpdate
        text: |-
               az elastic tag-rule create --monitor-name "myMonitor" --filtering-tags name="Environment" \
action="Include" value="Prod" --filtering-tags name="Environment" action="Exclude" value="Dev" --send-aad-logs false \
--send-activity-logs true --send-subscription-logs true --resource-group "myResourceGroup" --rule-set-name "default"
"""

helps['elastic tag-rule update'] = """
    type: command
    short-summary: "Update a tag rule set for a given monitor resource."
    parameters:
      - name: --filtering-tags
        short-summary: "List of filtering tags to be used for capturing logs. This only takes effect if \
SendActivityLogs flag is enabled. If empty, all resources will be captured. If only Exclude action is specified, the \
rules will apply to the list of all available resources. If Include actions are specified, the rules will only include \
resources with the associated tags."
        long-summary: |
            Usage: --filtering-tags name=XX value=XX action=XX

            name: The name (also known as the key) of the tag.
            value: The value of the tag.
            action: Valid actions for a filtering tag.

            Multiple actions can be specified by using more than one --filtering-tags argument.
"""

helps['elastic tag-rule delete'] = """
    type: command
    short-summary: "Delete a tag rule set for a given monitor resource."
    examples:
      - name: TagRules_Delete
        text: |-
               az elastic tag-rule delete --monitor-name "myMonitor" --resource-group "myResourceGroup" \
--rule-set-name "default"
"""

helps['elastic tag-rule wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the elastic tag-rule is met.
    examples:
      - name: Pause executing next line of CLI script until the elastic tag-rule is successfully deleted.
        text: |-
               az elastic tag-rule wait --monitor-name "myMonitor" --resource-group "myResourceGroup" --rule-set-name \
"default" --deleted
"""

helps['elastic vm-host'] = """
    type: group
    short-summary: Manage vm host with elastic
"""

helps['elastic vm-host list'] = """
    type: command
    short-summary: "List the vm resources currently being monitored by the Elastic monitor resource."
    examples:
      - name: VMHost_List
        text: |-
               az elastic vm-host list --monitor-name "myMonitor" --resource-group "myResourceGroup"
"""

helps['elastic vm-ingestion'] = """
    type: group
    short-summary: Manage vm ingestion with elastic
"""

helps['elastic vm-ingestion detail'] = """
    type: command
    short-summary: "List the vm ingestion details that will be monitored by the Elastic monitor resource."
    examples:
      - name: VMIngestion_Details
        text: |-
               az elastic vm-ingestion detail --monitor-name "myMonitor" --resource-group "myResourceGroup"
"""

helps['elastic vm-collection'] = """
    type: group
    short-summary: Manage vm collection with elastic
"""

helps['elastic vm-collection update'] = """
    type: command
    short-summary: "Update the vm details that will be monitored by the Elastic monitor resource."
    examples:
      - name: VMCollection_Update
        text: |-
               az elastic vm-collection update --monitor-name "myMonitor" --operation-name "Add" --vm-resource-id \
"/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtual\
machines/myVM" --resource-group "myResourceGroup"
"""
