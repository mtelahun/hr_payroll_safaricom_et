from odoo import api, fields, models


class HrEmployee(models.Model):

    _inherit = "hr.employee"

    # should be in-sync with field in res.company -> default_payroll_payment_gateway
    default_payroll_payment_gateway = fields.Selection(
        selection=[
                ('none', "None (Cash)"),
        ],
        default="_default_payroll_payment_gateway",
        string="Default Payroll Payment Gateway",
        help="The payment gateway to use when processing the employee's payslips for payment.",
        index=True,
        tracking=True,
    )

    @api.model
    def _default_payroll_payment_gateway(self):
        """ Return the default payment method chosen by the company. """
        return self.env.company.default_payroll_payment_gateway