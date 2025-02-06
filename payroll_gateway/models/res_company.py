from odoo import fields, models, _


class ResCompany(models.Model):

    _inherit="res.company"

    # should be in-sync with field in hr.employee -> payroll_payment_gateway
    payroll_payment_gateway = fields.Selection(
        selection=[
                ('none', _("None")),
                ('manual', _("Manual")),
        ],
        default='none',
        config_parameter="payroll.payroll_payment_gateway",
        string="Payroll Payment Gateway",
        help="The payment gateway to use when processing a payslip for payment.",
    )