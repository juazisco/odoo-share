# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsAxisLabel(models.Model):
    '''
    Mana Dashboard Echarts Axis Label
    '''
    _name = 'mana_dashboard.echarts_axis_label'

    show = fields.Boolean(string='Show', default=True)
    interval = fields.Integer(string='Interval', default=0)
    inside = fields.Boolean(string='Inside', default=False)
    rotate = fields.Integer(string='Rotate', default=0)
    margin = fields.Integer(string='Margin', default=8)
    formatter = fields.Char(string='Formatter', default='{value}')
    showMinLabel = fields.Boolean(string='Show Min Label', default=False)
    showMaxLabel = fields.Boolean(string='Show Max Label', default=False)
    hideOverlap = fields.Boolean(string='Hide Overlap', default=False)
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
            ('lighter', 'Lighter')],
        default='normal')
    fontFamily = fields.Char(string='Font Family', default='sans-serif')
    fontSize = fields.Integer(string='Font Size', default=12)
    align = fields.Selection(
        string='Align',
        selection=[
            ('left', 'Left'),
            ('center', 'Center'),
            ('right', 'Right')],
        default='center')
    verticalAlign = fields.Selection(
        string='Vertical Align',
        selection=[
            ('top', 'Top'),
            ('middle', 'Middle'),
            ('bottom', 'Bottom')],
        default='bottom')
    lineHeight = fields.Integer(string='Line Height', default=12)
    backgroundColor = fields.Char(string='Background Color', default='auto')
    borderColor = fields.Char(string='Border Color', default='#ccc')
    borderWidth = fields.Integer(string='Border Width', default=0)
    borderRadius = fields.Integer(string='Border Radius', default=0)
    padding = fields.Integer(string='Padding', default=0)
    shadowColor = fields.Char(string='Shadow Color', default='transparent')
    shadowBlur = fields.Integer(string='Shadow Blur', default=0)
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=0)
    width = fields.Char(string='Width', default='auto')
    height = fields.Char(string='Height', default='auto')
    textBorderColor = fields.Char(string='Text Border Color', default='transparent')
    textBorderWidth = fields.Integer(string='Text Border Width', default=0)
    textShadowColor = fields.Char(string='Text Shadow Color', default='transparent')
    textShadowBlur = fields.Integer(string='Text Shadow Blur', default=0)
    textShadowOffsetX = fields.Integer(string='Text Shadow Offset X', default=0)
    textShadowOffsetY = fields.Integer(string='Text Shadow Offset Y', default=0)
    ellipsis = fields.Boolean(string='Ellipsis', default=False)
    rich = fields.Many2Many(
        string='Rich',
        comodel_name='mana_dashboard.echarts_rich',
        relation='mana_dashboard_echarts_axis_label_rich_rel',
        column1='echarts_axis_label_id',
        column2='rich_id')



