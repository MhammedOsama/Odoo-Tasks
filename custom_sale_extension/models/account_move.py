
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model_create_multi
    def create(self, vals_list):
        moves = super().create(vals_list)
        moves._check_return_days()
        return moves

    @api.constrains('invoice_date', 'move_type')
    def _check_return_days(self):
        for move in self:
            if move.move_type == 'out_refund' and move.invoice_date:
                today = date.today()
                days_diff = (today - move.invoice_date).days
                
                return_days = int(self.env['ir.config_parameter'].sudo().get_param('custom_sale_extension.invoice_return_days', 30))
                
                if days_diff > return_days:
                    raise ValidationError('Cannot save credit note. The invoice date is %s days ago, which exceeds the allowed %s days.' % (days_diff, return_days))

