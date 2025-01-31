from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    # should be in-sync with field in hr.employee -> payroll_payment_gateway
    payroll_payment_gateway = fields.Selection(
        selection_add=[
                ('mpesa_et', "Safaricom M-PESA (ET)"),
        ],
    )