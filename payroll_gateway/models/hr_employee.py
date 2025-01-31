from odoo import api, fields, models, _


class HrEmployee(models.Model):

    _inherit = "hr.employee"

    @api.model
    def _get_payroll_payment_gateway(self):
        """ Return the default payment method chosen by the company. """
        return self.env.company.payroll_payment_gateway
    
    # should be in-sync with field in res.company -> payroll_payment_gateway
    payroll_payment_gateway = fields.Selection(
        selection=[
                ('none', _("None")),
        ],
        default=_get_payroll_payment_gateway,
        string="Payroll Payment Gateway",
        help="The payment gateway to use when processing the employee's payslips for payment.",
        index=True,
        tracking=True,
    )
