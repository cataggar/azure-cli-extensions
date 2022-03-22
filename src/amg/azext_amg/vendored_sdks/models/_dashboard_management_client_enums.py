# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from six import with_metaclass
from azure.core import CaseInsensitiveEnumMeta


class ActionType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates the action type. "Internal" refers to actions that are for internal only APIs.
    """

    INTERNAL = "Internal"

class CreatedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class IdentityType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The type 'SystemAssigned, UserAssigned' includes both an implicitly created identity and a set
    of user assigned identities. The type 'None' will remove any identities from the resource.
    """

    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"

class LastModifiedByType(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class Origin(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):
    """The intended executor of the operation.
    """

    USER = "user"
    SYSTEM = "system"
    USER_SYSTEM = "user,system"

class ProvisioningState(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    ACCEPTED = "Accepted"
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    DELETED = "Deleted"
    NOT_SPECIFIED = "NotSpecified"

class ZoneRedundancy(with_metaclass(CaseInsensitiveEnumMeta, str, Enum)):

    DISABLED = "Disabled"
    ENABLED = "Enabled"
