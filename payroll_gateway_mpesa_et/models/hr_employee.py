from odoo import api, fields, models


class HrEmployee(models.Model):

    _inherit = "hr.employee"

    # should be in-sync with field in res.company -> payroll_payment_gateway
    payroll_payment_gateway = fields.Selection(
        selection_add=[
            ('mpesa_et', "Safaricom M-PESA (ET)"),
        ],
    )

    mpesa_phone = fields.Text("M-PESA Telephone")
