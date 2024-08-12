from odoo import fields, models, api  # type: ignore

class TicketStatus(models.Model):
    _name = 'support.ticket.status'
    _description = 'Support Ticket Status'

    name = fields.Char(string="Name", required=True)

