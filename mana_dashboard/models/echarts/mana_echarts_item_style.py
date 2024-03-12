# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsItemStyle(models.Model):
    '''
    Mana Dashboard Item Style
    '''
    _name = 'mana_dashboard.echarts_item_style'

    color = fields.Char(string='Color', default='inherit')
    borderColor = fields.Char(string='Border Color', default='inherit')
    borderWidth = fields.Char(string='Border Width', default='auto')
    borderType = fields.Char(string='Border Type', default='inherit')
    borderDashOffset = fields.Char(string='Border Dash Offset', default='inherit')
    borderCap = fields.Char(string='Border Cap', default='inherit')
    borderJoin = fields.Char(string='Border Join', default='inherit')
    borderMiterLimit = fields.Char(string='Border Miter Limit', default='inherit')
    shadowBlur = fields.Integer(string='Shadow Blur', default=0)
    shadowColor = fields.Char(string='Shadow Color', default='transparent')
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=0)
    opacity = fields.Float(string='Opacity', default=1)
    decal = fields.Char(string='Decal', default='inherit')
