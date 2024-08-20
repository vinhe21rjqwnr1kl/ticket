from odoo import fields, models, api  # type: ignore

class TicketRespone(models.Model):
    _name = 'support.ticket.respone'
    _description = 'Support Ticket Respone'

    name = fields.Char(string="Name", required=True)
