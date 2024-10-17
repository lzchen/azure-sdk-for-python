# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.resource import PolicyClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-resource
# USAGE
    python create_or_update_policy_definition_version_at_management_group.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = PolicyClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.policy_definition_versions.create_or_update_at_management_group(
        management_group_name="MyManagementGroup",
        policy_definition_name="ResourceNaming",
        policy_definition_version="1.2.1",
        parameters={
            "properties": {
                "description": "Force resource names to begin with given 'prefix' and/or end with given 'suffix'",
                "displayName": "Enforce resource naming convention",
                "metadata": {"category": "Naming"},
                "mode": "All",
                "parameters": {
                    "prefix": {
                        "metadata": {"description": "Resource name prefix", "displayName": "Prefix"},
                        "type": "String",
                    },
                    "suffix": {
                        "metadata": {"description": "Resource name suffix", "displayName": "Suffix"},
                        "type": "String",
                    },
                },
                "policyRule": {
                    "if": {
                        "not": {"field": "name", "like": "[concat(parameters('prefix'), '*', parameters('suffix'))]"}
                    },
                    "then": {"effect": "deny"},
                },
                "version": "1.2.1",
            }
        },
    )
    print(response)


# x-ms-original-file: specification/resources/resource-manager/Microsoft.Authorization/stable/2023-04-01/examples/createOrUpdatePolicyDefinitionVersionAtManagementGroup.json
if __name__ == "__main__":
    main()
