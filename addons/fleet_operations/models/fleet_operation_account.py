# See LICENSE file for full copyright and licensing details.
"""Fleet Tenant, Res Partner Model."""

from odoo import fields, models


class AccountInvoice(models.Model):
    """Account Invoice Model."""

    _inherit = "account.move"

    vehicle_service_id = fields.Many2one(
        "fleet.vehicle.log.services", "Vehicle Service"
    )
    is_invoice_receive = fields.Boolean("Is Service Invoice Receive")
    is_invoice_return = fields.Boolean("Is Service Invoice Deposit")
