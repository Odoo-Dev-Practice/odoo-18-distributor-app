from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Add new fields
    country_of_origin_id = fields.Many2one('res.country', string='Country of Origin')