# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsSelectorLabel(models.Model):
    '''
    Mana Dashboard Selector Label
    '''
    _name = 'mana_dashboard.echarts_selector_label'

    show = fields.Boolean(string='Show', default=True)
    rotate = fields.Integer(string='Rotate', default=0)
    color = fields.Char(string='Color', default='#000')
    fontStyle = fields.Char(string='Font Style', default='normal')
    fontWeight = fields.Char(string='Font Weight', default='normal')
    fontFamily = fields.Char(string='Font Family', default='sans-serif')
    fontSize = fields.Integer(string='Font Size', default=12)
    align = fields.Selection(
        string='Align',
        selection=[
            ('auto', 'Auto'),
            ('left', 'Left'),
            ('right', 'Right')],
        default='auto')
    verticalAlign = fields.Selection(
        string='Vertical Align',
        selection=[
            ('auto', 'Auto'),
            ('top', 'Top'),
            ('bottom', 'Bottom')],
        default='auto')
    lineHeight = fields.Integer(string='Line Height', default=12)
    backgroundColor = fields.Char(string='Background Color', default='transparent')
    borderColor = fields.Char(string='Border Color', default='#ccc')
    borderWidth = fields.Integer(string='Border Width', default=0)
    borderType = fields.Selection(
        string='Border Type',
        selection=[
            ('solid', 'Solid'),
            ('dashed', 'Dashed'),
            ('dotted', 'Dotted')],
        default='solid')
    borderRadius = fields.Integer(string='Border Radius', default=0)
    padding = fields.Integer(string='Padding', default=5)
    shadowColor = fields.Char(string='Shadow Color', default='transparent')
    shadowBlur = fields.Integer(string='Shadow Blur', default=0)
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=0)
    width = fields.Integer(string='Width', default=50)
    height = fields.Integer(string='Height', default=50)
    textBorderColor = fields.Char(string='Text Border Color', default='transparent')
    textBorderWidth = fields.Integer(string='Text Border Width', default=0)
    textBorderType = fields.Selection(
        string='Text Border Type',
        selection=[
            ('solid', 'Solid'),
            ('dashed', 'Dashed'),
            ('dotted', 'Dotted')],
        default='solid')
    textShadowColor = fields.Char(string='Text Shadow Color', default='transparent')
    textShadowBlur = fields.Integer(string='Text Shadow Blur', default=0)
    textShadowOffsetX = fields.Integer(string='Text Shadow Offset X', default=0)
    textShadowOffsetY = fields.Integer(string='Text Shadow Offset Y', default=0)
    overflow = fields.Char(string='Overflow', default='truncate')
    ellipsis = fields.Char(string='Ellipsis', default='...')
    rich = fields.Many2Many(
        string='Rich',
        comodel_name='mana_dashboard.echarts_rich',
        relation='mana_dashboard_echarts_selector_label_rich_rel',
        column1='selector_label_id',
        column2='rich_id')
