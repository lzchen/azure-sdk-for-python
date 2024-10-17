# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.resource.aio import ApplicationClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestApplicationApplicationsOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(ApplicationClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get(self, resource_group):
        response = await self.client.applications.get(
            resource_group_name=resource_group.name,
            application_name="str",
            api_version="2019-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete(self, resource_group):
        response = await (
            await self.client.applications.begin_delete(
                resource_group_name=resource_group.name,
                application_name="str",
                api_version="2019-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update(self, resource_group):
        response = await (
            await self.client.applications.begin_create_or_update(
                resource_group_name=resource_group.name,
                application_name="str",
                parameters={
                    "kind": "str",
                    "applicationDefinitionId": "str",
                    "artifacts": [{"name": "str", "type": "str", "uri": "str"}],
                    "authorizations": [{"principalId": "str", "roleDefinitionId": "str"}],
                    "billingDetails": {"resourceUsageId": "str"},
                    "createdBy": {"applicationId": "str", "oid": "str", "puid": "str"},
                    "customerSupport": {"email": "str", "phone": "str", "contactName": "str"},
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"principalId": "str", "tenantId": "str"}},
                    },
                    "jitAccessPolicy": {
                        "jitAccessEnabled": bool,
                        "jitApprovalMode": "str",
                        "jitApprovers": [{"id": "str", "displayName": "str", "type": "str"}],
                        "maximumJitAccessDuration": "str",
                    },
                    "location": "str",
                    "managedBy": "str",
                    "managedResourceGroupId": "str",
                    "managementMode": "str",
                    "name": "str",
                    "outputs": {},
                    "parameters": {},
                    "plan": {
                        "name": "str",
                        "product": "str",
                        "publisher": "str",
                        "version": "str",
                        "promotionCode": "str",
                    },
                    "provisioningState": "str",
                    "publisherTenantId": "str",
                    "sku": {
                        "name": "str",
                        "capacity": 0,
                        "family": "str",
                        "model": "str",
                        "size": "str",
                        "tier": "str",
                    },
                    "supportUrls": {"governmentCloud": "str", "publicAzure": "str"},
                    "tags": {"str": "str"},
                    "type": "str",
                    "updatedBy": {"applicationId": "str", "oid": "str", "puid": "str"},
                },
                api_version="2019-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update(self, resource_group):
        response = await self.client.applications.update(
            resource_group_name=resource_group.name,
            application_name="str",
            api_version="2019-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_resource_group(self, resource_group):
        response = self.client.applications.list_by_resource_group(
            resource_group_name=resource_group.name,
            api_version="2019-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_list_by_subscription(self, resource_group):
        response = self.client.applications.list_by_subscription(
            api_version="2019-07-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_get_by_id(self, resource_group):
        response = await self.client.applications.get_by_id(
            application_id="str",
            api_version="2019-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_delete_by_id(self, resource_group):
        response = await (
            await self.client.applications.begin_delete_by_id(
                application_id="str",
                api_version="2019-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_create_or_update_by_id(self, resource_group):
        response = await (
            await self.client.applications.begin_create_or_update_by_id(
                application_id="str",
                parameters={
                    "kind": "str",
                    "applicationDefinitionId": "str",
                    "artifacts": [{"name": "str", "type": "str", "uri": "str"}],
                    "authorizations": [{"principalId": "str", "roleDefinitionId": "str"}],
                    "billingDetails": {"resourceUsageId": "str"},
                    "createdBy": {"applicationId": "str", "oid": "str", "puid": "str"},
                    "customerSupport": {"email": "str", "phone": "str", "contactName": "str"},
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"principalId": "str", "tenantId": "str"}},
                    },
                    "jitAccessPolicy": {
                        "jitAccessEnabled": bool,
                        "jitApprovalMode": "str",
                        "jitApprovers": [{"id": "str", "displayName": "str", "type": "str"}],
                        "maximumJitAccessDuration": "str",
                    },
                    "location": "str",
                    "managedBy": "str",
                    "managedResourceGroupId": "str",
                    "managementMode": "str",
                    "name": "str",
                    "outputs": {},
                    "parameters": {},
                    "plan": {
                        "name": "str",
                        "product": "str",
                        "publisher": "str",
                        "version": "str",
                        "promotionCode": "str",
                    },
                    "provisioningState": "str",
                    "publisherTenantId": "str",
                    "sku": {
                        "name": "str",
                        "capacity": 0,
                        "family": "str",
                        "model": "str",
                        "size": "str",
                        "tier": "str",
                    },
                    "supportUrls": {"governmentCloud": "str", "publicAzure": "str"},
                    "tags": {"str": "str"},
                    "type": "str",
                    "updatedBy": {"applicationId": "str", "oid": "str", "puid": "str"},
                },
                api_version="2019-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_update_by_id(self, resource_group):
        response = await self.client.applications.update_by_id(
            application_id="str",
            api_version="2019-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_begin_refresh_permissions(self, resource_group):
        response = await (
            await self.client.applications.begin_refresh_permissions(
                resource_group_name=resource_group.name,
                application_name="str",
                api_version="2019-07-01",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
