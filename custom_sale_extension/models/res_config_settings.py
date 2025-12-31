from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    invoice_return_days = fields.Integer(
        string='Number of Days for Invoice Return',
        config_parameter='custom_sale_extension.invoice_return_days',
        default=5,
    )

