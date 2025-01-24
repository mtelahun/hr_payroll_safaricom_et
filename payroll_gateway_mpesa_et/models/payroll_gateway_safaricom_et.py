from base64 import b64encode
from json import loads
from requests import codes, request

from odoo import fields, models


class PayrollGatewaySafaricomEt(models.Model):

    _name = "payroll.gateway.safaricom_et"
    _description = "Safaricom Ethiopia Payroll Integration"

    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("enabled", "Enabled"),
            ("disabled", "Disabled"),
        ],
        string="Status",
        readonly=True,
        copy=False,
        default="draft",
        tracking=True,
        help="""* When the gateway is created the status is \'Draft\'
        \n* If the gateway should process payslips the status is \'Enabled\'.
        \n* If the gateway should NOT process payslips the status is \'Disabled\'.""",
    )
    
    name = fields.Char(readonly=True, states={"draft": [("readonly", False)]})

    api_key = fields.Char(readonly=True, copy=False)

    api_secret = fields.Char(readonly=True, copy=False)

    auth_endpoint = fields.Char(name="Authentication Endpoint")
    
    grant_type = fields.Char(default="client_credentials")

    payout_endpoint = fields.Char(name="Payout Endpoint")

    result_url = fields.Char()
 
    timeout_url = fields.Char()
 
    initiator_name = fields.Char(name="API User")
 
    security_credential = fields.Char(name="API Password")
 
    party_a = fields.Char(name="Business Shortcode")

    def authenticate(self) -> dict[str, str]:

        grant_type = "".join("grant_type=", self.grant_type)
        endpoint = "".join(self.auth_endpoint, "?", grant_type)
        authorization = "".join("Bearer ", b64encode("".join(self.api_key, ":", self.api_secret).encode('utf-8')))
        headers = {'Authorization': authorization}
        response = request("GET", endpoint, headers=headers)

        if response.status_code == codes.ok:
            return loads(response.json())
        else:
            response.raise_for_status()
    
    def get_authorization(self, auth_response: dict[str, str]) -> str:
        bearer_auth = "".join(auth_response["token_type"]).join(" ").join(auth_response["access_token"])
        
        return bearer_auth
    
    def payout(self, bearer_auth: str, party_b: str, amount: float, remarks: str) -> dict[str, str]:

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