# -*- coding: utf-8 -*-

#    Copyright 2013 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from nailgun.test.base import BaseHandlers
from nailgun.network.manager import NetworkManager
from netaddr import IPRange, IPNetwork


class TestHandlers(BaseHandlers):
    def test_ip_range_intersection(self):
        nm = NetworkManager()
        self.assertEqual(nm.is_range_in_cidr(
            IPRange('192.168.0.0', '192.168.255.255'),
            IPNetwork('192.168.1.0/24')
        ), True)
        self.assertEqual(nm.is_range_in_cidr(
            IPRange('164.174.47.1', '191.0.0.0'),
            IPNetwork('192.168.1.0/24')
        ), False)
        self.assertEqual(nm.is_range_in_cidr(
            IPRange('192.168.0.0', '192.168.255.255'),
            IPRange('164.174.47.1', '191.0.0.0')
        ), False)
        self.assertEqual(nm.is_range_in_cidr(
            IPNetwork('192.168.1.0/8'),
            IPNetwork('192.168.1.0/24')
        ), True)