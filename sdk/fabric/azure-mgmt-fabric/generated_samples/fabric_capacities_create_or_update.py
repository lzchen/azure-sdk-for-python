# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.fabric import FabricMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-fabric
# USAGE
    python fabric_capacities_create_or_update.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = FabricMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="SUBSCRIPTION_ID",
    )

    response = client.fabric_capacities.begin_create_or_update(
        resource_group_name="TestRG",
        capacity_name="azsdktest",
        resource={
            "location": "westcentralus",
            "properties": {"administration": {"members": ["azsdktest@microsoft.com", "azsdktest2@microsoft.com"]}},
            "sku": {"name": "F2", "tier": "Fabric"},
        },
    ).result()
    print(response)


# x-ms-original-file: 2023-11-01/FabricCapacities_CreateOrUpdate.json
if __name__ == "__main__":
    main()
