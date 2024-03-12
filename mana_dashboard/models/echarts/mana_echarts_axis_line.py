# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsAxisLine(models.Model):
    '''
    Mana Dashboard Echarts Axis Line
    '''
    _name = 'mana_dashboard.echarts_axis_line'

    show = fields.Boolean(string='Show', default=True)
    onZero = fields.Boolean(string='On Zero', default=True)
    onZeroAxisIndex = fields.Integer(string='On Zero Axis Index', default=0)
    symbol = fields.Char(string='Symbol', default='none')
    symbolSize = fields.Char(string='Symbol Size', default='[10, 15]')
    symbolOffset = fields.Char(string='Symbol Offset', default='[0, 0]')
    lineStyle = fields.Many2one(
        string='Line Style',
        comodel_name='mana_dashboard.echarts_line_style',
        ondelete='restrict')
