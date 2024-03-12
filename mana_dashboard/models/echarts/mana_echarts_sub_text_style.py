# -*- coding: utf-8 -*-

from odoo import models, fields, _


class ManaEchartsSubTextStyle(models.Model):
    '''
    Mana Dashboard Sub Text Style
    '''
    _name = 'mana_dashboard.echarts_sub_text_style'

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
    aign = fields.Char(string='Align', default='left')
    verticalAlign = fields.Char(string='Vertical Align', default='middle')
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
    rich = fields.Many2many(
        string='Rich',
        comodel_name='mana_dashboard.echarts_text_style_rich',
        relation='mana_dashboard_echarts_text_style_rich_rel',
        column1='text_style_id',
        column2='rich_id')
    textAlign = fields.Selection(
        string='Text Align',
        selection=[
            ('auto', 'Auto'),
            ('left', 'Left'),
            ('right', 'Right'),
            ('center', 'Center')],
        default='auto')
    textVerticalAlign = fields.Selection(
        string='Text Vertical Align',
        selection=[
            ('auto', 'Auto'),
            ('top', 'Top'),
            ('bottom', 'Bottom'),
            ('middle', 'Middle')],
        default='auto')
    triggerEvent = fields.Boolean(string='Trigger Event', default=False)
    textVerticalAlign = fields.Selection(
        string='Text Vertical Align',
        selection=[
            ('auto', 'Auto'),
            ('top', 'Top'),
            ('bottom', 'Bottom'),
            ('middle', 'Middle')],
        default='auto')
    padding = fields.Integer(string='Padding', default=0)
    itemGap = fields.Integer(string='Item Gap', default=0)
    zlevel = fields.Integer(string='Z Level', default=0)
    left = fields.Char(string='Left', default='auto')
    top = fields.Char(string='Top', default='auto')
    right = fields.Char(string='Right', default='auto')
    bottom = fields.Char(string='Bottom', default='auto')
    backgroundColor = fields.Char(string='Background Color', default='transparent')
    borderColor = fields.Char(string='Border Color', default='#ccc')
    borderWidth = fields.Integer(string='Border Width', default=0)
    borderRadius = fields.Integer(string='Border Radius', default=0)
    shadowBlur = fields.Integer(string='Shadow Blur', default=0)
    shadowColor = fields.Char(string='Shadow Color', default='transparent')
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=0)
