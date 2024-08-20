from odoo import fields, models, api  # type: ignore

class Ticket(models.Model):
    _name = 'support.ticket'
    _description = 'Support Ticket'
    _rec_name = 'ticket_code'

    is_customer = fields.Boolean(string="Is Customer")

    ################################
    #                              #
    #      Basic information       #
    #                              #
    ################################
    ticket_code = fields.Char(string="Ticket Code",
                              readonly=True,
                              computed="_compute_ticket_code",
                              store=True,
                              help="Ticket Code"
                              )
    ticket_title = fields.Char(string="Ticker Title",
                               required=True,
                               help="Ticket Title"
                               )
    create_date = fields.Date(string="Start Day", default=fields.Date.today())
    nearest_response_date = fields.Date(string="Response Day")
    stage = fields.Many2one('support.ticket.stage',
                            string="Ticket Stage",
                            group_expand="_read_group_stage"  # for getting all the stage
                            )
    content = fields.Text(string="Ticket description", help="Description")

    status = fields.Many2one('support.ticket.status', string="Status")

    color = fields.Integer(related='status.color', string="Color")
    ticket_response = fields.One2many('support.ticket', string="Ticket Respone")
    note = fields.Text(string="Note")

    # internal user
    user = fields.Many2many('res.users', string="User")
    user_image = fields.Binary(related='user.image_1920', string='User Image')

    ####################
    #                  #
    #     customer     #
    #                  #
    ####################
    customer_id = fields.Many2one('res.partner', string="Customer")
    email = fields.Char(string="Email", related="customer_id.email")
    phone = fields.Char(string="Phone", related="customer_id.phone")
    website = fields.Char(string="Website", related="customer_id.website")












    @api.model
    def _read_group_stage(self, group, domain,order):
        return self.env['support.ticket.status'].search([])


    def action_send_email(self):
        mail_template = self.env.ref('real-estate-ads.offer_mail_template')
        mail_template.send_mail(self.id, force_send=True)

    @api.depends('id')
    def _compute_ticket_code(self):
        pass

