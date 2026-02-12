from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    payroll_payment_gateway = fields.Selection(
        related='company_id.payroll_payment_gateway',
        string="Default Payroll Payment Gateway",
        readonly=False,
        default_model="res_company"
    )