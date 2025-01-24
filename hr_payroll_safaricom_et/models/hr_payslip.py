from odoo import fields, models


class HrPayslip(models.Model):

    _name = "hr.payslip.safaricom_et"
    _inherit = "hr.payslip"

    safaricom_et_payment_response = fields.Many2One("payslip.safaricom_et.response")

    safaricom_et_payment_result = fields.Many2One("payslip.safaricom_et.result")

    def payslip_cancel(self):
 
         return super(HrPayslip, self).payslip_cancel()

    def unlink(self):
 
         return super(HrPayslip, self).unlink()

    def action_payslip_payment(self):

        return super(HrPayslip, self).action_payslip_payment()
