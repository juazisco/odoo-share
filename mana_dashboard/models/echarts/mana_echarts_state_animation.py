# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsStateAnimation(models.Model):
    '''
    Mana Dashboard State Animation
    '''
    _name = 'mana_dashboard.echarts_state_animation'

    duration = fields.Integer(string='Duration', default=300)
    easing = fields.Char(string='Easing', default='cubicOut')
