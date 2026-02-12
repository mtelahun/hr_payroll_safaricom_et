from odoo.http import Controller, Response, route

class TimeoutController(Controller):
    @route('/payroll_gateway_mpesa_et/timeout', type='json', auth='public', website=False, methods=['POST'], csrf=False)
    def handler(self):
        Response.render()
