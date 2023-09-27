from odoo import fields, models
from dateutil.relativedelta import relativedelta
class Estate(models.Model):
    _name = "estate"
    _description = "Housing Management"

    name = fields.Char(default="Unknown")
    last_seen = fields.Datetime("Last Seen", default=lambda self: fields.Datetime.now())
    bedrooms = fields.Integer("Bedrooms", default=2)
    default_availability = fields.Date("Default Availability", default=lambda self: fields.Date.today() + relativedelta(months=3), copy=False)
    active = fields.Boolean(default=True)
    state = fields.Selection[
        ('new', "New Offer")
        ('offer_received', "Offer received")
        ('offer_accepted', "Offer accepted")
        ('sold', "Sold")
        ('cancel', "Cancelled")
    ],
    string="Status", readonly=True, copy=False, tracking=3, default='new)'
