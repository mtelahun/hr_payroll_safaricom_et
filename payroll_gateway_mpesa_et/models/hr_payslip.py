import logging

from odoo import api, fields, models, _
from odoo.exceptions import UserError


_logger = logging.getLogger(__name__)

class HrPayslip(models.Model):

     _name = "hr.payslip.safaricom_et"
     _inherit = "hr.payslip"

     # should be in-sync with field in res.company and hr.employee -> default_payroll_payment_gateway
     payroll_payment_gateway = fields.Selection(
          selection_add=[
                    ('mpesa_et', "Safaricom M-PESA (ET)"),
          ],
     )
    
     paid_mpesa = fields.Boolean(
          string="M-Pesa Payment",
          readonly=True,
          copy=False,
          states={"draft": [("readonly", False)]},
     )

     safaricom_et_payment_response = fields.Many2One("payslip.safaricom_et.response")

     safaricom_et_payment_result = fields.Many2One("payslip.safaricom_et.result")

     @api.onchange("paid_mpesa")
     def onchange_paid_mpesa(self):
            self.paid = self.paid_mpesa

     def refund_sheet(self):
          
          return super(HrPayslip, self).refund_sheet()
     
     def payslip_cancel(self):
     
               if self.filtered(lambda slip: slip.paid_mpesa):
                    raise UserError(_("Cannot cancel a payslip that is already paid through M-Pesa."))
          
               return super(HrPayslip, self).payslip_cancel()

     def unlink(self):
     
               if self.filtered(lambda slip: slip.paid_mpesa):
                    raise UserError(_("Cannot delete a payslip that is already paid through M-Pesa."))
     
               return super(HrPayslip, self).unlink()

     def action_payslip_payment(self):
     
               if self.filtered(lambda slip: slip.paid_mpesa or slip.paid):
                    _logger.warning("One or more Payslips have already been marked as paid")
               
               for slip in self:
                    if slip.paid_mpesa or slip.paid:
                         _logger.warning("Payslip %s already marked as paid", slip.number)
                         continue


               return super(HrPayslip, self).action_payslip_payment()
