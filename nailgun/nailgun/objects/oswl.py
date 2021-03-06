#    Copyright 2015 Mirantis, Inc.
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


from nailgun.db import db
from nailgun.db.sqlalchemy import models
from nailgun.objects import NailgunCollection
from nailgun.objects import NailgunObject


class OpenStackWorkloadStats(NailgunObject):

    #: SQLAlchemy model for OpenStackWorkloadStats
    model = models.OpenStackWorkloadStats

    @classmethod
    def get_last_by(cls, cluster_id, resource_type):
        """Get last entry by cluster_id and resource type.
        """
        instance = db().query(models.OpenStackWorkloadStats) \
            .order_by(models.OpenStackWorkloadStats.created_date.desc()) \
            .filter_by(cluster_id=cluster_id) \
            .filter_by(resource_type=resource_type) \
            .first()

        return instance


class OpenStackWorkloadStatsCollection(NailgunCollection):
    single = OpenStackWorkloadStats
