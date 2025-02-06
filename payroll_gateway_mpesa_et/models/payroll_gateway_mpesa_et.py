from base64 import b64encode
from json import loads
from requests import codes, request
from typing import Dict

from odoo import fields, models


class PayrollGatewayMpesaEt(models.Model):

    _name = "payroll.gateway.mpesa_et"
    _description = "Safaricom Ethiopia M-PESA Payroll Integration"

    enabled = fields.Boolean(
        copy=False,
        help="""* If the gateway should process payslips the status should be \'Enabled\'.
        \n* If the gateway should NOT process payslips the status should be \'Disabled\'.""",
    )
    
    name = fields.Char(readonly="enabled == true")

    api_key = fields.Char(string="API Key", readonly="enabled == true", copy=False)

    api_secret = fields.Char(string="API Secret", readonly="enabled == true", copy=False)

    auth_endpoint = fields.Char(name="Authentication Endpoint", readonly="enabled == true")
    
    grant_type = fields.Char(default="client_credentials", readonly=True)

    payout_endpoint = fields.Char(name="Payout Endpoint", readonly="enabled == true")

    result_url = fields.Char(name="Result URL", readonly="enabled == true")
 
    timeout_url = fields.Char(name="Timeout URL", readonly="enabled == true")
 
    initiator_name = fields.Char(name="API User", readonly="enabled == true")
 
    security_credential = fields.Char(name="API Password", readonly="enabled == true")
 
    party_a = fields.Char(name="Business Shortcode", readonly="enabled == true")

    def authenticate(self) -> Dict[str, str]:

        grant_type = "".join("grant_type=", self.grant_type)
        endpoint = "".join(self.auth_endpoint, "?", grant_type)
        authorization = "".join("Bearer ", b64encode("".join(self.api_key, ":", self.api_secret).encode('utf-8')))
        headers = {'Authorization': authorization}
        response = request("GET", endpoint, headers=headers)

        if response.status_code == codes.ok:
            return loads(response.json())
        else:
            response.raise_for_status()
    
    def get_authorization(self, auth_response: Dict[str, str]) -> str:
        bearer_auth = "".join(auth_response["token_type"]).join(" ").join(auth_response["access_token"])
        
        return bearer_auth
    
    def payout(self, bearer_auth: str, party_b: str, amount: float, remarks: str) -> Dict[str, str]:

        command = "SalaryPayment"
        occasion = "Disbursement"
        headers = {"Authorization": bearer_auth}
        endpoint = "".join(self.payout_endpoint)
        payload = {
            "InitiatorName": self.initiator_name,
            "SecurityCredential": self.security_credential,
            "Occassion": occasion,
            "CommandID": command,
            "PartyA": self.party_a,
            "PartyB": party_b,
            "Remarks": remarks,
            "Amount": amount,
            "QueueTimeOutURL": self.timeout_url,
            "ResultURL": self.result_url
        }
        response = request("POST", endpoint, headers=headers, data=payload)

        if response.status_code == codes.ok:
            return loads(response.json())
        else:
            response.raise_for_status()

    def translate_payment_response(self, response: Dict[str, str]) -> Dict[str, str]:

       return {
           "ok_conversation": response["ConversationId"],
           "ok_originator_conversation": response["OriginatorConversationID"],
           "ok_response_code": response["ResponseCode"],
           "ok_response_desc": response["ResponseDescription"],
           "raw": response.__str__
       }
