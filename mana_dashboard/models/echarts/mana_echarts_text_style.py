# -*- coding: utf-8 -*-

from odoo import models, fields, _


class TextStyle(models.Model):
    '''
    Mana Dashboard Text Style
    '''
    _name = 'mana_dashboard.echarts_text_style'

    color = fields.Char(string='Color', default='#000')
    fontStyle = fields.Selection(
        string='Font Style',
        selection=[
            ('normal', 'Normal'),
            ('italic', 'Italic'),
            ('oblique', 'Oblique')],
        default='normal')
    fontWeight = fields.Selection(
        string='Font Weight',
        selection=[
            ('normal', 'Normal'),
            ('bold', 'Bold'),
            ('bolder', 'Bolder'),
            ('lighter', 'Lighter'),
            ('100', '100'),
            ('200', '200'),
            ('300', '300'),
            ('400', '400'),
            ('500', '500'),
            ('custom', 'Custom')],
        default='normal')
    customFontWeight = fields.Integer(string='Custom Font Weight', default=400)
    fontFamily = fields.Char(string='Font Family', default='sans-serif')
    fontSize = fields.Integer(string='Font Size', default=18)
    lineHeight = fields.Integer(string='Line Height', default=18)
    width = fields.Integer(string='Width', default=0)
    height = fields.Integer(string='Height', default=0)
    textBorderColor = fields.Char(string='Text Border Color', default='transparent')
    textBorderWidth = fields.Integer(string='Text Border Width', default=0)
    textShadowColor = fields.Char(string='Text Shadow Color', default='transparent')
    textShadowBlur = fields.Integer(string='Text Shadow Blur', default=0)
    textShadowOffsetX = fields.Integer(string='Text Shadow Offset X', default=0)
    textShadowOffsetY = fields.Integer(string='Text Shadow Offset Y', default=0)
    overflow = fields.Char(string='Overflow', default='truncate')
    ellipsis = fields.Boolean(string='Ellipsis', default=True)
