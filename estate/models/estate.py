from odoo import fields, models
class Estate(models.Model):
    _name = "estate"
    _description = "Housing Management"

    name = fields.Char()