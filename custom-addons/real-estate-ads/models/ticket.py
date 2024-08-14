from odoo import fields, models, api  # type: ignore

class Ticket(models.Model):
    _name = 'support.ticket'
    _description = 'Support Ticket'
    
    ticket_id = fields.Char(string="Ticket")
    customer_id = fields.Char(string="Customer")
    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email")
    content = fields.Text(string="Content")
    ticket_type = fields.Many2one('support.ticket.type', string="Ticket Type")
    ticket_respone = fields.Many2one('support.ticket.respone', string="Ticket Respone")
    create_day = fields.Date(default=fields.Date.today(), string="Start Day")
    respone_day = fields.Date(string="Respone Day")
    deadline = fields.Date(string="DeadLine")
    status = fields.Many2one('support.ticket.status', string="Ticket Status", group_expand="_read_group_status", required=True)
    user = fields.Many2many('res.users', string="User")
    user_image = fields.Binary(related='user.image_1920', string='User Image')


    
    

    @api.model
    def _read_group_status(self, group, domain,order):
        return self.env['support.ticket.status'].search([])
    
    def action_send_email(self):
        mail_template = self.env.ref('real-estate-ads.offer_mail_template')
        mail_template.send_mail(self.id, force_send=True)
    



