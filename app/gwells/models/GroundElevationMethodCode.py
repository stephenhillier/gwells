"""
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
from django.db import models

from gwells.models.audit_model import AuditModel


class GroundElevationMethodCode(AuditModel):
    """
    The method used to determine the ground elevation of a well.
    Some examples of methods to determine ground elevation include:
    GPS, Altimeter, Differential GPS, Level, 1:50,000 map, 1:20,000 map, 1:10,000 map, 1:5,000 map.
    """
    ground_elevation_method_code = models.CharField(primary_key=True, max_length=10, editable=False)
    description = models.CharField(max_length=100)
    display_order = models.PositiveIntegerField()

    effective_date = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'ground_elevation_method_code'
        ordering = ['display_order', 'description']

    def __str__(self):
        return self.description
