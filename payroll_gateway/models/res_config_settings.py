from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    default_payroll_payment_gateway = fields.Selection(
        related='company_id.default_payroll_payment_gateway',
        string="Default Payroll Payment Gateway",
        readonly=False,
    )