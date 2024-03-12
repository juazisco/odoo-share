# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsRich(models.Model):
    '''
    Mana Dashboard Rich
    '''
    _name = 'mana_dashboard.echarts_rich'

    name = fields.Char(string='Name', required=True)
    color = fields.Char(string='Color', default='#000')
    fontStyle = fields.Char(string='Font Style', default='normal')
    fontColor = fields.Char(string='Font Color', default='#fff')
    fontWeight = fields.Char(string='Font Weight', default='normal')
    fontFamily = fields.Char(string='Font Family', default='sans-serif')
    fontSize = fields.Integer(string='Font Size', default=12)
    align = fields.Char(string='Align', default='center')
    verticalAlign = fields.Char(string='Vertical Align', default='middle')
    lineHeight = fields.Integer(string='Line Height', default=12)
    backgroundColor = fields.Char(string='Background Color', default='transparent')
    borderColor = fields.Char(string='Border Color', default='transparent')
    borderWidth = fields.Integer(string='Border Width', default=0)
    borderType = fields.Char(string='Border Type', default='solid')
    borderDashOffset = fields.Integer(string='Border Dash Offset', default=0)
    borderRadius = fields.Integer(string='Border Radius', default=0)
    padding = fields.Integer(string='Padding', default=0)
    shadowColor = fields.Char(string='Shadow Color', default='transparent')
    shadowBlur = fields.Integer(string='Shadow Blur', default=0)
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=0)
    width = fields.Integer(string='Width', default=0)
    height = fields.Integer(string='Height', default=0)
    textBorderColor = fields.Char(string='Text Border Color', default='transparent')
    textBorderWidth = fields.Integer(string='Text Border Width', default=0)
    textBorderStyle = fields.Char(string='Text Border Style', default='solid')
    textBorderDashOffset = fields.Integer(string='Text Border Dash Offset', default=0)
    textShadowColor = fields.Char(string='Text Shadow Color', default='transparent')
    textShadowBlur = fields.Integer(string='Text Shadow Blur', default=0)
    textShadowOffsetX = fields.Integer(string='Text Shadow Offset X', default=0)
    textShadowOffsetY = fields.Integer(string='Text Shadow Offset Y', default=0)
