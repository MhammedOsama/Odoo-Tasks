from odoo import http
from odoo.http import Response, request

class SaleOrderController(http.Controller):

    @http.route('/api/sale_orders/latest', methods=['GET'], type='http', auth='public', csrf=False)
    def get_latest_orders(self):
        orders = request.env['sale.order'].sudo().search([], limit=10, order='id desc')
        result = []
        for order in orders:
            result.append({
                'name': order.name,
                'partner_id': order.partner_id.name if order.partner_id else False,
                'amount_total': order.amount_total,
                'delivery_note': order.delivery_note or '',
            })
        return request.make_json_response(result)
        