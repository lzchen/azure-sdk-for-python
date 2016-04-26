# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class CertificateOrderAction(Resource):
    """
    Represents a certificate action

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param kind: Kind of resource
    :type kind: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param certificate_order_action_type: Type. Possible values include:
     'CertificateIssued', 'CertificateOrderCanceled',
     'CertificateOrderCreated', 'CertificateRevoked',
     'DomainValidationComplete', 'FraudDetected', 'OrgNameChange',
     'OrgValidationComplete', 'SanDrop'
    :type certificate_order_action_type: str
    :param created_at: Time at which the certificate action was performed
    :type created_at: datetime
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'certificate_order_action_type': {'key': 'properties.type', 'type': 'CertificateOrderActionType'},
        'created_at': {'key': 'properties.createdAt', 'type': 'iso-8601'},
    }

    def __init__(self, location, id=None, name=None, kind=None, type=None, tags=None, certificate_order_action_type=None, created_at=None):
        super(CertificateOrderAction, self).__init__(id=id, name=name, kind=kind, location=location, type=type, tags=tags)
        self.certificate_order_action_type = certificate_order_action_type
        self.created_at = created_at
