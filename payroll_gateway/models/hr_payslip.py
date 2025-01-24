from odoo import api, fields, models


class HrPayslip(models.Model):

    _inherit = "hr.payslip"

     # should be in-sync with field in res.company and hr.employee -> default_payroll_payment_gateway
    payroll_payment_gateway = fields.Selection(
        selection=[
                ('none', "None (Cash)"),
        ],
        default="_default_payroll_payment_gateway",
        string="Payroll Payment Gateway",
        help="The payment gateway to use when processing the payslip for payment.",
        index=True,
        tracking=True,
    )

    @api.model
    def _default_payroll_payment_gateway(self):
        """ Return the default payment method chosen by the company. """
        return self.env.company.default_payroll_payment_gateway
    
    @api.onchange("employee_id")
    def onchange_employee_id(self):
        self.payroll_payment_gateway = self.employee_id.default_payroll_payment_gateway