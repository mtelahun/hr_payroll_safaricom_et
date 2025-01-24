from odoo import fields, models


class PayslipSafaricomEtResult(models.Model):

    _name = "payslip.safaricom_et.result"
    _description = "Safaricom Ethiopia Payslip Integration Result"

    result_type = fields.Integer(readonly=True)

    result_code = fields.Integer(readonly=True)

    result_desc = fields.Text(readonly=True)

    originiator_conversation = fields.Text(name="OriginatorConversationID", readonly=True)

    conversation = fields.Text(name="ConversationID", readonly=True)

    result_parameters = fields.MultilineText(readonly=True)
    