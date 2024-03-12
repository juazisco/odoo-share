# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsLineStyle(models.Model):
    '''
    Mana Dashboard Echarts Line Style
    '''
    _name = 'mana_dashboard.echarts_line_style'

    color = fields.Char(string='Color', default='inherit')
    width = fields.Char(string='Width', default='auto')
    type = fields.Char(string='Type', default='inherit')
    dashOffset = fields.Char(string='Dash Offset', default='inherit')
    cap = fields.Char(string='Cap', default='inherit')
    join = fields.Char(string='Join', default='inherit')
    miterLimit = fields.Char(string='Miter Limit', default='inherit')
    shadowBlur = fields.Char(string='Shadow Blur', default='inherit')
    shadowColor = fields.Char(string='Shadow Color', default='transparent')
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=0)
    opacity = fields.Float(string='Opacity', default=1)