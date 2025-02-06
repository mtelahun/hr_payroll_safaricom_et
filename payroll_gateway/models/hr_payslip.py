import logging

from odoo import api, fields, models
from odoo.tools.translate import _

_logger = logging.getLogger(__name__)


class HrPayslip(models.Model):

    _inherit = "hr.payslip"
    
    state = fields.Selection(
        selection_add=[
            ("payment", "Payment"),
            ("done",)
        ],
        help="""* When the payslip is created the status is \'Draft\'
        \n* If the payslip is under verification, the status is \'Waiting\'.
        \n* If the payslip is in the process of being paid, the status is \'Payment\'.
        \n* If the payslip is paid then status is set to \'Done\'.
        \n* When user cancel payslip the status is \'Rejected\'.""",
    )

    @api.model
    def _get_payroll_payment_gateway(self):
        """ Return the default payment method chosen by the company. """
        return self.env.company.payroll_payment_gateway

     # should be in-sync with field in res.company and hr.employee -> payroll_payment_gateway
    payroll_payment_gateway = fields.Selection(
        selection=[
                ('none', _("None")),
                ('manual', _("Manual")),
        ],
        default=_get_payroll_payment_gateway,
        string="Payroll Payment Gateway",
        help="The payment gateway to use when processing the payslip for payment.",
        index=True,
        tracking=True,
    )
    
    @api.onchange("employee_id")
    def onchange_employee_id(self):
        self.payroll_payment_gateway = self.employee_id.payroll_payment_gateway

    def action_payslip_confirm(self):
        if (
            not self.env.context.get("without_compute_sheet")
            and not self.prevent_compute_on_confirm
        ):
            self.compute_sheet()
        return self.write({"state": "payment"})

    def action_payslip_payment(self):
        for slip in self:
            if slip.paid:
                _logger.warning(
                    "Payslip %s (%s) is already 'Paid'. Discontinuing any further processing.",
                    slip.name,
                    slip.number
                )
                continue
            if slip.payroll_payment_gateway == 'manual':
                continue
            elif slip.payroll_payment_gateway == 'none':
                slip.action_payslip_done()


    def action_payslip_done(self):
        return self.write({"state": "done"})
