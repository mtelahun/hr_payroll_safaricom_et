from odoo.http import Controller, Response, route

class ResultController(Controller):
    @route('/payroll_gateway_mpesa_et/result', type='json', auth='public', website=False, methods=['POST'], csrf=False)
    def handler(self):
        Response.render()
