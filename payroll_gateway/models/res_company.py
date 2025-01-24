from odoo import fields, models


class ResCompany(models.Model):

    _inherit="res.company"

    # should be in-sync with field in hr.employee -> default_payroll_payment_gateway
    default_payroll_payment_gateway = fields.Selection(
        selection=[
                ('none', "None (Cash)"),
        ],
        default='none',
        config_parameter="payroll.default_payment_gateway",
        string="Default Payroll Payment Gateway",
        help="The payment gateway to use when processing a payslip for payment.",
        tracking=True,
    )