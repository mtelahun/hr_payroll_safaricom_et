from odoo import api, fields, models


class HrEmployee(models.Model):

    _inherit = "hr.employee"

    # should be in-sync with field in res.company -> default_payroll_payment_gateway
    default_payroll_payment_gateway = fields.Selection(
        selection_add=[
                ('mpesa_et', "Safaricom M-PESA (ET)"),
        ],
    )
