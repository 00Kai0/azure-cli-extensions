# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class Resource(msrest.serialization.Model):
    """Definition of a Resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified identifier of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~maintenance_management_client.models.SystemData
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None


class ApplyUpdate(Resource):
    """Apply Update request.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified identifier of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~maintenance_management_client.models.SystemData
    :param status: The status. Possible values include: "Pending", "InProgress", "Completed",
     "RetryNow", "RetryLater".
    :type status: str or ~maintenance_management_client.models.UpdateStatus
    :param resource_id: The resourceId.
    :type resource_id: str
    :param last_update_time: Last Update time.
    :type last_update_time: ~datetime.datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
        'last_update_time': {'key': 'properties.lastUpdateTime', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ApplyUpdate, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.resource_id = kwargs.get('resource_id', None)
        self.last_update_time = kwargs.get('last_update_time', None)


class ConfigurationAssignment(Resource):
    """Configuration Assignment.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified identifier of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~maintenance_management_client.models.SystemData
    :param location: Location of the resource.
    :type location: str
    :param maintenance_configuration_id: The maintenance configuration Id.
    :type maintenance_configuration_id: str
    :param resource_id: The unique resourceId.
    :type resource_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'location': {'key': 'location', 'type': 'str'},
        'maintenance_configuration_id': {'key': 'properties.maintenanceConfigurationId', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ConfigurationAssignment, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.maintenance_configuration_id = kwargs.get('maintenance_configuration_id', None)
        self.resource_id = kwargs.get('resource_id', None)


class ErrorDetails(msrest.serialization.Model):
    """An error response details received from the Azure Maintenance service.

    :param code: Service-defined error code. This code serves as a sub-status for the HTTP error
     code specified in the response.
    :type code: str
    :param message: Human-readable representation of the error.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDetails, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)


class InputLinuxParameters(msrest.serialization.Model):
    """Input properties for patching a Linux machine.

    :param package_name_masks_to_exclude: Package names to be excluded for patching.
    :type package_name_masks_to_exclude: list[str]
    :param package_name_masks_to_include: Package names to be included for patching.
    :type package_name_masks_to_include: list[str]
    :param classifications_to_include: Classification category of patches to be patched.
    :type classifications_to_include: list[str]
    """

    _attribute_map = {
        'package_name_masks_to_exclude': {'key': 'packageNameMasksToExclude', 'type': '[str]'},
        'package_name_masks_to_include': {'key': 'packageNameMasksToInclude', 'type': '[str]'},
        'classifications_to_include': {'key': 'classificationsToInclude', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InputLinuxParameters, self).__init__(**kwargs)
        self.package_name_masks_to_exclude = kwargs.get('package_name_masks_to_exclude', None)
        self.package_name_masks_to_include = kwargs.get('package_name_masks_to_include', None)
        self.classifications_to_include = kwargs.get('classifications_to_include', None)


class InputPatchConfiguration(msrest.serialization.Model):
    """Input configuration for a patch run.

    :param reboot_setting: Possible reboot preference as defined by the user based on which it
     would be decided to reboot the machine or not after the patch operation is completed. Possible
     values include: "IfRequired", "Never", "Always". Default value: "IfRequired".
    :type reboot_setting: str or ~maintenance_management_client.models.RebootOptions
    :param windows_parameters: Input parameters specific to patching a Windows machine. For Linux
     machines, do not pass this property.
    :type windows_parameters: ~maintenance_management_client.models.InputWindowsParameters
    :param linux_parameters: Input parameters specific to patching Linux machine. For Windows
     machines, do not pass this property.
    :type linux_parameters: ~maintenance_management_client.models.InputLinuxParameters
    :param pre_tasks: List of pre tasks. e.g. [{'source' :'runbook', 'taskScope': 'Global',
     'parameters': { 'arg1': 'value1'}}].
    :type pre_tasks: list[~maintenance_management_client.models.TaskProperties]
    :param post_tasks: List of post tasks. e.g. [{'source' :'runbook', 'taskScope': 'Resource',
     'parameters': { 'arg1': 'value1'}}].
    :type post_tasks: list[~maintenance_management_client.models.TaskProperties]
    """

    _attribute_map = {
        'reboot_setting': {'key': 'rebootSetting', 'type': 'str'},
        'windows_parameters': {'key': 'windowsParameters', 'type': 'InputWindowsParameters'},
        'linux_parameters': {'key': 'linuxParameters', 'type': 'InputLinuxParameters'},
        'pre_tasks': {'key': 'tasks.preTasks', 'type': '[TaskProperties]'},
        'post_tasks': {'key': 'tasks.postTasks', 'type': '[TaskProperties]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InputPatchConfiguration, self).__init__(**kwargs)
        self.reboot_setting = kwargs.get('reboot_setting', "IfRequired")
        self.windows_parameters = kwargs.get('windows_parameters', None)
        self.linux_parameters = kwargs.get('linux_parameters', None)
        self.pre_tasks = kwargs.get('pre_tasks', None)
        self.post_tasks = kwargs.get('post_tasks', None)


class InputWindowsParameters(msrest.serialization.Model):
    """Input properties for patching a Windows machine.

    :param kb_numbers_to_exclude: Windows KBID to be excluded for patching.
    :type kb_numbers_to_exclude: list[str]
    :param kb_numbers_to_include: Windows KBID to be included for patching.
    :type kb_numbers_to_include: list[str]
    :param classifications_to_include: Classification category of patches to be patched.
    :type classifications_to_include: list[str]
    :param exclude_kbs_requiring_reboot: Exclude patches which need reboot.
    :type exclude_kbs_requiring_reboot: bool
    """

    _attribute_map = {
        'kb_numbers_to_exclude': {'key': 'kbNumbersToExclude', 'type': '[str]'},
        'kb_numbers_to_include': {'key': 'kbNumbersToInclude', 'type': '[str]'},
        'classifications_to_include': {'key': 'classificationsToInclude', 'type': '[str]'},
        'exclude_kbs_requiring_reboot': {'key': 'excludeKbsRequiringReboot', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InputWindowsParameters, self).__init__(**kwargs)
        self.kb_numbers_to_exclude = kwargs.get('kb_numbers_to_exclude', None)
        self.kb_numbers_to_include = kwargs.get('kb_numbers_to_include', None)
        self.classifications_to_include = kwargs.get('classifications_to_include', None)
        self.exclude_kbs_requiring_reboot = kwargs.get('exclude_kbs_requiring_reboot', None)


class ListApplyUpdate(msrest.serialization.Model):
    """Response for ApplyUpdate list.

    :param value: The list of apply updates.
    :type value: list[~maintenance_management_client.models.ApplyUpdate]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ApplyUpdate]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ListApplyUpdate, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ListConfigurationAssignmentsResult(msrest.serialization.Model):
    """Response for ConfigurationAssignments list.

    :param value: The list of configuration Assignments.
    :type value: list[~maintenance_management_client.models.ConfigurationAssignment]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ConfigurationAssignment]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ListConfigurationAssignmentsResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ListMaintenanceConfigurationsResult(msrest.serialization.Model):
    """Response for MaintenanceConfigurations list.

    :param value: The list of maintenance Configurations.
    :type value: list[~maintenance_management_client.models.MaintenanceConfiguration]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MaintenanceConfiguration]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ListMaintenanceConfigurationsResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ListUpdatesResult(msrest.serialization.Model):
    """Response for Updates list.

    :param value: The pending updates.
    :type value: list[~maintenance_management_client.models.Update]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Update]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ListUpdatesResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class MaintenanceConfiguration(Resource):
    """Maintenance configuration record type.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified identifier of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource.
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~maintenance_management_client.models.SystemData
    :param location: Gets or sets location of the resource.
    :type location: str
    :param tags: A set of tags. Gets or sets tags of the resource.
    :type tags: dict[str, str]
    :param namespace: Gets or sets namespace of the resource.
    :type namespace: str
    :param extension_properties: Gets or sets extensionProperties of the maintenanceConfiguration.
    :type extension_properties: dict[str, str]
    :param maintenance_scope: Gets or sets maintenanceScope of the configuration. Possible values
     include: "Host", "OSImage", "Extension", "InGuestPatch", "SQLDB", "SQLManagedInstance".
    :type maintenance_scope: str or ~maintenance_management_client.models.MaintenanceScope
    :param visibility: Gets or sets the visibility of the configuration. The default value is
     'Custom'. Possible values include: "Custom", "Public".
    :type visibility: str or ~maintenance_management_client.models.Visibility
    :param install_patches: The input parameters to be passed to the patch run operation.
    :type install_patches: ~maintenance_management_client.models.InputPatchConfiguration
    :param start_date_time: Effective start date of the maintenance window in YYYY-MM-DD hh:mm
     format. The start date can be set to either the current date or future date. The window will be
     created in the time zone provided and adjusted to daylight savings according to that time zone.
    :type start_date_time: str
    :param expiration_date_time: Effective expiration date of the maintenance window in YYYY-MM-DD
     hh:mm format. The window will be created in the time zone provided and adjusted to daylight
     savings according to that time zone. Expiration date must be set to a future date. If not
     provided, it will be set to the maximum datetime 9999-12-31 23:59:59.
    :type expiration_date_time: str
    :param duration: Duration of the maintenance window in HH:mm format. If not provided, default
     value will be used based on maintenance scope provided. Example: 05:00.
    :type duration: str
    :param time_zone: Name of the timezone. List of timezones can be obtained by executing
     [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell. Example: Pacific Standard Time, UTC,
     W. Europe Standard Time, Korea Standard Time, Cen. Australia Standard Time.
    :type time_zone: str
    :param recur_every: Rate at which a Maintenance window is expected to recur. The rate can be
     expressed as daily, weekly, or monthly schedules. Daily schedule are formatted as recurEvery:
     [Frequency as integer]['Day(s)']. If no frequency is provided, the default frequency is 1.
     Daily schedule examples are recurEvery: Day, recurEvery: 3Days.  Weekly schedule are formatted
     as recurEvery: [Frequency as integer]['Week(s)'] [Optional comma separated list of weekdays
     Monday-Sunday]. Weekly schedule examples are recurEvery: 3Weeks, recurEvery: Week
     Saturday,Sunday. Monthly schedules are formatted as [Frequency as integer]['Month(s)'] [Comma
     separated list of month days] or [Frequency as integer]['Month(s)'] [Week of Month (First,
     Second, Third, Fourth, Last)] [Weekday Monday-Sunday] [Optional Offset(No. of days)]. Offset
     value must be between -6 to 6 inclusive. Monthly schedule examples are recurEvery: Month,
     recurEvery: 2Months, recurEvery: Month day23,day24, recurEvery: Month Last Sunday, recurEvery:
     Month Fourth Monday, recurEvery: Month Last Sunday Offset-3, recurEvery: Month Third Sunday
     Offset6.
    :type recur_every: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'system_data': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'namespace': {'key': 'properties.namespace', 'type': 'str'},
        'extension_properties': {'key': 'properties.extensionProperties', 'type': '{str}'},
        'maintenance_scope': {'key': 'properties.maintenanceScope', 'type': 'str'},
        'visibility': {'key': 'properties.visibility', 'type': 'str'},
        'install_patches': {'key': 'properties.installPatches', 'type': 'InputPatchConfiguration'},
        'start_date_time': {'key': 'properties.maintenanceWindow.startDateTime', 'type': 'str'},
        'expiration_date_time': {'key': 'properties.maintenanceWindow.expirationDateTime', 'type': 'str'},
        'duration': {'key': 'properties.maintenanceWindow.duration', 'type': 'str'},
        'time_zone': {'key': 'properties.maintenanceWindow.timeZone', 'type': 'str'},
        'recur_every': {'key': 'properties.maintenanceWindow.recurEvery', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MaintenanceConfiguration, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.namespace = kwargs.get('namespace', None)
        self.extension_properties = kwargs.get('extension_properties', None)
        self.maintenance_scope = kwargs.get('maintenance_scope', None)
        self.visibility = kwargs.get('visibility', None)
        self.install_patches = kwargs.get('install_patches', None)
        self.start_date_time = kwargs.get('start_date_time', None)
        self.expiration_date_time = kwargs.get('expiration_date_time', None)
        self.duration = kwargs.get('duration', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.recur_every = kwargs.get('recur_every', None)


class MaintenanceError(msrest.serialization.Model):
    """An error response received from the Azure Maintenance service.

    :param error: Details of the error.
    :type error: ~maintenance_management_client.models.ErrorDetails
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDetails'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MaintenanceError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class Operation(msrest.serialization.Model):
    """Represents an operation returned by the GetOperations request.

    :param name: Name of the operation.
    :type name: str
    :param display: Display name of the operation.
    :type display: ~maintenance_management_client.models.OperationInfo
    :param origin: Origin of the operation.
    :type origin: str
    :param properties: Properties of the operation.
    :type properties: object
    :param is_data_action: Indicates whether the operation is a data action.
    :type is_data_action: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationInfo'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'object'},
        'is_data_action': {'key': 'isDataAction', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.origin = kwargs.get('origin', None)
        self.properties = kwargs.get('properties', None)
        self.is_data_action = kwargs.get('is_data_action', None)


class OperationInfo(msrest.serialization.Model):
    """Information about an operation.

    :param provider: Name of the provider.
    :type provider: str
    :param resource: Name of the resource type.
    :type resource: str
    :param operation: Name of the operation.
    :type operation: str
    :param description: Description of the operation.
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationInfo, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class OperationsListResult(msrest.serialization.Model):
    """Result of the List Operations operation.

    :param value: A collection of operations.
    :type value: list[~maintenance_management_client.models.Operation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationsListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource. Possible values
     include: "User", "Application", "ManagedIdentity", "Key".
    :type created_by_type: str or ~maintenance_management_client.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: ~datetime.datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :type last_modified_by_type: str or ~maintenance_management_client.models.CreatedByType
    :param last_modified_at: The timestamp of resource last modification (UTC).
    :type last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = kwargs.get('created_by', None)
        self.created_by_type = kwargs.get('created_by_type', None)
        self.created_at = kwargs.get('created_at', None)
        self.last_modified_by = kwargs.get('last_modified_by', None)
        self.last_modified_by_type = kwargs.get('last_modified_by_type', None)
        self.last_modified_at = kwargs.get('last_modified_at', None)


class TaskProperties(msrest.serialization.Model):
    """Task properties of the software update configuration.

    :param parameters: Gets or sets the parameters of the task.
    :type parameters: dict[str, str]
    :param source: Gets or sets the name of the runbook.
    :type source: str
    :param task_scope: Global Task execute once when schedule trigger. Resource task execute for
     each VM. Possible values include: "Global", "Resource". Default value: "Global".
    :type task_scope: str or ~maintenance_management_client.models.TaskScope
    """

    _attribute_map = {
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'source': {'key': 'source', 'type': 'str'},
        'task_scope': {'key': 'taskScope', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TaskProperties, self).__init__(**kwargs)
        self.parameters = kwargs.get('parameters', None)
        self.source = kwargs.get('source', None)
        self.task_scope = kwargs.get('task_scope', "Global")


class Update(msrest.serialization.Model):
    """Maintenance update on a resource.

    :param maintenance_scope: The impact area. Possible values include: "Host", "OSImage",
     "Extension", "InGuestPatch", "SQLDB", "SQLManagedInstance".
    :type maintenance_scope: str or ~maintenance_management_client.models.MaintenanceScope
    :param impact_type: The impact type. Possible values include: "None", "Freeze", "Restart",
     "Redeploy".
    :type impact_type: str or ~maintenance_management_client.models.ImpactType
    :param status: The status. Possible values include: "Pending", "InProgress", "Completed",
     "RetryNow", "RetryLater".
    :type status: str or ~maintenance_management_client.models.UpdateStatus
    :param impact_duration_in_sec: Duration of impact in seconds.
    :type impact_duration_in_sec: int
    :param not_before: Time when Azure will start force updates if not self-updated by customer
     before this time.
    :type not_before: ~datetime.datetime
    :param resource_id: The resourceId.
    :type resource_id: str
    """

    _attribute_map = {
        'maintenance_scope': {'key': 'maintenanceScope', 'type': 'str'},
        'impact_type': {'key': 'impactType', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'impact_duration_in_sec': {'key': 'impactDurationInSec', 'type': 'int'},
        'not_before': {'key': 'notBefore', 'type': 'iso-8601'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Update, self).__init__(**kwargs)
        self.maintenance_scope = kwargs.get('maintenance_scope', None)
        self.impact_type = kwargs.get('impact_type', None)
        self.status = kwargs.get('status', None)
        self.impact_duration_in_sec = kwargs.get('impact_duration_in_sec', None)
        self.not_before = kwargs.get('not_before', None)
        self.resource_id = kwargs.get('resource_id', None)
