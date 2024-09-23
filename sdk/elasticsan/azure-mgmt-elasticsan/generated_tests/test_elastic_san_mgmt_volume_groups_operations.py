# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.elasticsan import ElasticSanMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestElasticSanMgmtVolumeGroupsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ElasticSanMgmtClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_list_by_elastic_san(self, resource_group):
        response = self.client.volume_groups.list_by_elastic_san(
            resource_group_name=resource_group.name,
            elastic_san_name="str",
            api_version="2024-05-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_create(self, resource_group):
        response = self.client.volume_groups.begin_create(
            resource_group_name=resource_group.name,
            elastic_san_name="str",
            volume_group_name="str",
            parameters={
                "id": "str",
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "name": "str",
                "properties": {
                    "encryption": "str",
                    "encryptionProperties": {
                        "identity": {"userAssignedIdentity": "str"},
                        "keyVaultProperties": {
                            "currentVersionedKeyExpirationTimestamp": "2020-02-20 00:00:00",
                            "currentVersionedKeyIdentifier": "str",
                            "keyName": "str",
                            "keyVaultUri": "str",
                            "keyVersion": "str",
                            "lastKeyRotationTimestamp": "2020-02-20 00:00:00",
                        },
                    },
                    "enforceDataIntegrityCheckForIscsi": bool,
                    "networkAcls": {"virtualNetworkRules": [{"id": "str", "action": "Allow"}]},
                    "privateEndpointConnections": [
                        {
                            "properties": {
                                "privateLinkServiceConnectionState": {
                                    "actionsRequired": "str",
                                    "description": "str",
                                    "status": "str",
                                },
                                "groupIds": ["str"],
                                "privateEndpoint": {"id": "str"},
                                "provisioningState": "str",
                            },
                            "id": "str",
                            "name": "str",
                            "systemData": {
                                "createdAt": "2020-02-20 00:00:00",
                                "createdBy": "str",
                                "createdByType": "str",
                                "lastModifiedAt": "2020-02-20 00:00:00",
                                "lastModifiedBy": "str",
                                "lastModifiedByType": "str",
                            },
                            "type": "str",
                        }
                    ],
                    "protocolType": "str",
                    "provisioningState": "str",
                },
                "systemData": {
                    "createdAt": "2020-02-20 00:00:00",
                    "createdBy": "str",
                    "createdByType": "str",
                    "lastModifiedAt": "2020-02-20 00:00:00",
                    "lastModifiedBy": "str",
                    "lastModifiedByType": "str",
                },
                "type": "str",
            },
            api_version="2024-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_update(self, resource_group):
        response = self.client.volume_groups.begin_update(
            resource_group_name=resource_group.name,
            elastic_san_name="str",
            volume_group_name="str",
            parameters={
                "identity": {
                    "type": "str",
                    "principalId": "str",
                    "tenantId": "str",
                    "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                },
                "properties": {
                    "encryption": "str",
                    "encryptionProperties": {
                        "identity": {"userAssignedIdentity": "str"},
                        "keyVaultProperties": {
                            "currentVersionedKeyExpirationTimestamp": "2020-02-20 00:00:00",
                            "currentVersionedKeyIdentifier": "str",
                            "keyName": "str",
                            "keyVaultUri": "str",
                            "keyVersion": "str",
                            "lastKeyRotationTimestamp": "2020-02-20 00:00:00",
                        },
                    },
                    "enforceDataIntegrityCheckForIscsi": bool,
                    "networkAcls": {"virtualNetworkRules": [{"id": "str", "action": "Allow"}]},
                    "protocolType": "str",
                },
            },
            api_version="2024-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_begin_delete(self, resource_group):
        response = self.client.volume_groups.begin_delete(
            resource_group_name=resource_group.name,
            elastic_san_name="str",
            volume_group_name="str",
            api_version="2024-05-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_get(self, resource_group):
        response = self.client.volume_groups.get(
            resource_group_name=resource_group.name,
            elastic_san_name="str",
            volume_group_name="str",
            api_version="2024-05-01",
        )

        # please add some check logic here by yourself
        # ...
