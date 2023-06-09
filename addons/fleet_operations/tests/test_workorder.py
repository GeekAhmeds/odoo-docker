# See LICENSE file for full copyright and licensing details.

from datetime import datetime

from odoo.tests import tagged
from odoo.tests.common import TransactionCase
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT


@tagged("-standard", "test_rj")
class TestWorkOrder(TransactionCase):
    def setUp(self):
        super(TestWorkOrder, self).setUp()

    def test(self):
        self.vehicle_obj = self.env["fleet.vehicle"]
        fleet_brand = self.env.ref("fleet.brand_audi")
        fleet_model = self.env.ref("fleet.model_a1")
        self.service_obj = self.env["fleet.vehicle.log.services"]
        self.env.ref("fleet.type_service_service_1")
        workshop_id = self.env.ref("base.res_partner_1")
        cr_dt = datetime.today().strftime(DEFAULT_SERVER_DATETIME_FORMAT)

        self.vehicle = self.vehicle_obj.create(
            {
                "f_brand_id": fleet_brand.id,
                "model_id": fleet_model.id,
                "license_plate": "MH-04-7777",
                "odometer": 3000,
                "odometer_unit": "kilometers",
                "fuel_type": "diesel",
            }
        )
        self.assertTrue(self.vehicle, "vehicle Type not created")
        self.workorder = self.service_obj.create(
            {
                "vehicle_id": self.vehicle.id,
                # 'cost_subtype_id': service_cost_id.id,
                "amount": 2000,
                "priority": "normal",
                "date_complete": cr_dt,
                "team_id": workshop_id.id,
            }
        )
        self.assertTrue(self.workorder, "workorder not created")
