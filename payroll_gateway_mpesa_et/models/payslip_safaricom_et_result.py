from odoo import fields, models


class PayslipSafaricomEtResult(models.Model):

    _name = "payslip.mpesa.safaricom_et.result"
    _description = "Safaricom Ethiopia M-PESA Payslip Integration Result"

    result_type = fields.Integer(readonly=True)

    result_code = fields.Integer(readonly=True)

    result_desc = fields.Text(readonly=True)

    originator_conversation = fields.Text(string="OriginatorConversationID", readonly=True)

    conversation = fields.Text(string="ConversationID", readonly=True)

    result_parameters = fields.MultilineText(readonly=True)

    tx_amount = fields.Decimal(string="Transaction Amount", readonly=True)

    tx_receipt = fields.Text(string="Transaction Receipt", readonly=True)

    tx_completed_at = fields.DateTime(string="Transaction Completed At", readonly=True)

    recepient_public_name = fields.Text(readonly=True)
    
    recepient_is_registered_customer = fields.Bool(readonly=True)
