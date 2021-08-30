# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AddressPrefixType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Address prefix type.
    """

    IP_PREFIX = "IPPrefix"
    SERVICE_TAG = "ServiceTag"

class AdminRuleKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether the rule is custom or default.
    """

    CUSTOM = "Custom"
    DEFAULT = "Default"

class ConfigurationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Configuration Deployment Type.
    """

    SECURITY_ADMIN = "SecurityAdmin"
    SECURITY_USER = "SecurityUser"
    CONNECTIVITY = "Connectivity"

class ConnectivityTopology(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Connectivity topology type.
    """

    HUB_AND_SPOKE = "HubAndSpoke"
    MESH = "Mesh"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DeleteExistingNSGs(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Flag if need to delete existing network security groups.
    """

    FALSE = "False"
    TRUE = "True"

class DeleteExistingPeering(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Flag if need to remove current existing peerings.
    """

    FALSE = "False"
    TRUE = "True"

class DeploymentStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Deployment Status.
    """

    NOT_STARTED = "NotStarted"
    DEPLOYING = "Deploying"
    DEPLOYED = "Deployed"
    FAILED = "Failed"

class EffectiveAdminRuleKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether the rule is custom or default.
    """

    CUSTOM = "Custom"
    DEFAULT = "Default"

class EffectiveUserRuleKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether the rule is custom or default.
    """

    CUSTOM = "Custom"
    DEFAULT = "Default"

class GroupConnectivity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Group connectivity type.
    """

    NONE = "None"
    DIRECTLY_CONNECTED = "DirectlyConnected"

class IsGlobal(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Flag if global mesh is supported.
    """

    FALSE = "False"
    TRUE = "True"

class MembershipType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Membership Type.
    """

    STATIC = "Static"
    DYNAMIC = "Dynamic"

class MemberType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Group member type.
    """

    VIRTUAL_NETWORK = "VirtualNetwork"
    SUBNET = "Subnet"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The current provisioning state.
    """

    SUCCEEDED = "Succeeded"
    UPDATING = "Updating"
    DELETING = "Deleting"
    FAILED = "Failed"

class SecurityConfigurationRuleAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether network traffic is allowed or denied.
    """

    ALLOW = "Allow"
    DENY = "Deny"
    ALWAYS_ALLOW = "AlwaysAllow"

class SecurityConfigurationRuleDirection(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The direction of the rule. The direction specifies if the rule will be evaluated on incoming or
    outgoing traffic.
    """

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"

class SecurityConfigurationRuleProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Network protocol this rule applies to.
    """

    TCP = "Tcp"
    UDP = "Udp"
    ICMP = "Icmp"
    ESP = "Esp"
    ANY = "Any"
    AH = "Ah"

class SecurityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Security Type.
    """

    ADMIN_POLICY = "AdminPolicy"
    USER_POLICY = "UserPolicy"

class UseHubGateway(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Flag if need to use hub gateway.
    """

    FALSE = "False"
    TRUE = "True"

class UserRuleKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether the rule is custom or default.
    """

    CUSTOM = "Custom"
    DEFAULT = "Default"
