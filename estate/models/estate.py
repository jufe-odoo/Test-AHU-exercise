from odoo import fields, models
class Estate(models.Model):
    _name = "estate"
    _description = "Housing Management"

    name = fields.Char(default="Unknown")
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    bedrooms = fields.Integer("Bedrooms", default=2)
    default_availability = fields.Date("Default Availability", default=lambda self: fields.Date.today(90))
