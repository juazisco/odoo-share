# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsPageTextStyle(models.Model):
    '''
    Mana Dashboard Echarts Page Text Style
    '''
    _name = 'mana_dashboard.echarts_page_text_style'

    color = fields.Char(string='Color', default='#333')
    fontStyle = fields.Char(string='Font Style', default='normal')
    fontWeight = fields.Char(string='Font Weight', default='normal')
    fontFamily = fields.Char(string='Font Family', default='sans-serif')
    fontSize = fields.Integer(string='Font Size', default=12)
    lineHeight = fields.Integer(string='Line Height', default=12)
    width = fields.Integer(string='Width', default=50)
    height = fields.Integer(string='Height', default=50)
    textBorderColor = fields.Char(string='Text Border Color', default='transparent')
    textBorderWidth = fields.Integer(string='Text Border Width', default=0)
    textShadowColor = fields.Char(string='Text Shadow Color', default='transparent')
    textShadowBlur = fields.Integer(string='Text Shadow Blur', default=0)
    textShadowOffsetX = fields.Integer(string='Text Shadow Offset X', default=0)
    textShadowOffsetY = fields.Integer(string='Text Shadow Offset Y', default=0)
    overflow = fields.Char(string='Overflow', default='truncate')
    ellipsis = fields.Char(string='Ellipsis', default='...')
