# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsPolar(models.Model):
    '''
    Mana Dashboard Echarts Title
    '''
    _name = 'mana_dashboard.echarts_polar'

    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=2)
    center = fields.Char(string='Center', default='center')
    radius = fields.Char(string='Radius', default='75%')
    tooltip = fields.Many2one(
        string='Tooltip',
        comodel_name='mana_dashboard.echarts_tooltip',
        ondelete='restrict')

