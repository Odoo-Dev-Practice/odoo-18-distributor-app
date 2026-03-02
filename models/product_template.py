from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # General
    country_of_origin_id = fields.Many2one('res.country', string='Country of Origin', help='Country of Origin')

    # Cartonization
    units_per_master_carton = fields.Integer(string='Units per Master Carton', help='Number of units per master carton')
    units_per_inner_carton = fields.Integer(string='Units per Inner Carton', help='Number of units per inner carton')

    # Shipping
    cbm_per_box = fields.Float(string='CBM per BOX', digits=(16,4), help='Cubic Meter per BOX')
    gross_weight_per_box = fields.Float(string='Gross Weight per BOX', digits=(16,4), help='Gross Weight per BOX')