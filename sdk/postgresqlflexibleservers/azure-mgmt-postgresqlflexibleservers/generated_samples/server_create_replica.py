# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.postgresqlflexibleservers import PostgreSQLManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-postgresqlflexibleservers
# USAGE
    python server_create_replica.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = PostgreSQLManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="ffffffff-ffff-ffff-ffff-ffffffffffff",
    )

    response = client.servers.begin_create(
        resource_group_name="testrg",
        server_name="pgtestsvc5rep",
        parameters={
            "identity": {
                "type": "UserAssigned",
                "userAssignedIdentities": {
                    "/subscriptions/ffffffff-ffff-ffff-ffff-ffffffffffff/resourceGroups/testresourcegroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/test-usermanagedidentity": {}
                },
            },
            "location": "westus",
            "properties": {
                "createMode": "Replica",
                "dataEncryption": {
                    "geoBackupKeyURI": "",
                    "geoBackupUserAssignedIdentityId": "",
                    "primaryKeyURI": "https://test-kv.vault.azure.net/keys/test-key1/77f57315bab34b0189daa113fbc78787",
                    "primaryUserAssignedIdentityId": "/subscriptions/ffffffff-ffff-ffff-ffff-ffffffffffff/resourceGroups/testresourcegroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/test-usermanagedidentity",
                    "type": "AzureKeyVault",
                },
                "pointInTimeUTC": "2021-06-27T00:04:59.4078005+00:00",
                "sourceServerResourceId": "/subscriptions/ffffffff-ffff-ffff-ffff-ffffffffffff/resourceGroups/testrg/providers/Microsoft.DBforPostgreSQL/flexibleServers/sourcepgservername",
            },
        },
    ).result()
    print(response)


# x-ms-original-file: specification/postgresql/resource-manager/Microsoft.DBforPostgreSQL/stable/2024-08-01/examples/ServerCreateReplica.json
if __name__ == "__main__":
    main()
