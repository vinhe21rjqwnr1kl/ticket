'''
Author: Thinh dep trai
Model Description: 
'''

from odoo import models, fields


class stage(models.Model):
    _name = 'support.ticket.stage'
    _description = ''


    name = fields.Char(string="Name", required=True)