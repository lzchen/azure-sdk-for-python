# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.resource import DeploymentStacksClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-resource
# USAGE
    python deployment_stack_management_group_validate.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DeploymentStacksClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.deployment_stacks.begin_validate_stack_at_management_group(
        management_group_id="myMg",
        deployment_stack_name="simpleDeploymentStack",
        deployment_stack={
            "location": "eastus",
            "properties": {
                "actionOnUnmanage": {"managementGroups": "detach", "resourceGroups": "detach", "resources": "detach"},
                "denySettings": {
                    "applyToChildScopes": False,
                    "excludedActions": ["action"],
                    "excludedPrincipals": ["principal"],
                    "mode": "denyDelete",
                },
                "parameters": {"parameter1": {"value": "a string"}},
                "templateLink": {"uri": "https://example.com/exampleTemplate.json"},
            },
            "tags": {"tagkey": "tagVal"},
        },
    ).result()
    print(response)


# x-ms-original-file: specification/resources/resource-manager/Microsoft.Resources/stable/2024-03-01/examples/DeploymentStackManagementGroupValidate.json
if __name__ == "__main__":
    main()
