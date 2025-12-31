from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_note = fields.Text(string='Delivery Note')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('delivery_note'):
                vals['delivery_note'] = 'Auto-generated delivery note'
        return super().create(vals_list)

