import logging

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class HrPayslip(models.Model):

     _inherit = "hr.payslip"

     # should be in-sync with field in res.company and hr.employee -> payroll_payment_gateway
     payroll_payment_gateway = fields.Selection(
          selection_add = [
               ('mpesa_et', "Safaricom M-PESA (ET)"),
          ]
     )
    
     paid_mpesa = fields.Boolean(
          string="M-PESA Payment",
          readonly=True,
          copy=False,
          states={"draft": [("readonly", False)]},
     )

     safaricom_et_payment_response = fields.Many2one("payslip.safaricom_et.response")

     safaricom_et_payment_result = fields.Many2one("payslip.safaricom_et.result")

     @api.onchange("paid_mpesa")
     def onchange_paid_mpesa(self):
          self.paid = self.paid_mpesa

     def refund_sheet(self):
          
          return super(HrPayslip, self).refund_sheet()
     
     def payslip_cancel(self):
     
          if self.filtered(lambda slip: slip.paid_mpesa):
               raise ValidationError(_("Cannot cancel a payslip that is already paid through M-Pesa."))
     
          return super(HrPayslip, self).payslip_cancel()

     def unlink(self):
     
          if self.filtered(lambda slip: slip.paid_mpesa):
               raise ValidationError(_("Cannot delete a payslip that is already paid through M-Pesa."))

          return super(HrPayslip, self).unlink()

     def action_payslip_payment(self):
               
          for slip in self:
               if slip.payroll_payment_gateway == 'mpesa_et':
                    # Gateway


          return super(HrPayslip, self).action_payslip_payment()
