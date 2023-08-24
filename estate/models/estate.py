from odoo import fields, models
class Estate(models.Model):
    _name = "Estate"
    _description = "Housing Management"

    name = fields.char()