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
    python deployment_stack_subscription_validate.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DeploymentStacksClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.deployment_stacks.begin_validate_stack_at_subscription(
        deployment_stack_name="simpleDeploymentStack",
        deployment_stack={
            "location": "eastus",
            "properties": {
                "actionOnUnmanage": {"managementGroups": "delete", "resourceGroups": "delete", "resources": "delete"},
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


# x-ms-original-file: specification/resources/resource-manager/Microsoft.Resources/stable/2024-03-01/examples/DeploymentStackSubscriptionValidate.json
if __name__ == "__main__":
    main()
