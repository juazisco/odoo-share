# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsAxisTick(models.Model):
    '''
    Mana Dashboard Echarts Axis Tick
    '''
    _name = 'mana_dashboard.echarts_axis_tick'

    show = fields.Boolean(string='Show', default=True)
    alignWithLabel = fields.Boolean(string='Align With Label', default=False)
    interval = fields.Integer(string='Interval', default=0)
    inside = fields.Boolean(string='Inside', default=False)
    length = fields.Integer(string='Length', default=5)
    lineStyle = fields.Many2one(
        string='Line Style',
        comodel_name='mana_dashboard.echarts_line_style',
        ondelete='restrict')

