# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsItemStyle(models.Model):
    '''
    Mana Dashboard Item Style
    '''
    _name = 'mana_dashboard.echarts_split_line'

    show = fields.Boolean(string='Show', default=True)
    interval = fields.Integer(string='Interval', default=0)
    lineStyle = fields.Many2one(
        string='Line Style',
        comodel_name='mana_dashboard.echarts_line_style',
        ondelete='restrict')
    color = fields.Char(string='Color', default='#ccc')
    width = fields.Integer(string='Width', default=1)
    type = fields.Selection(
        string='Type',
        selection=[
            ('solid', 'Solid'),
            ('dashed', 'Dashed'),
            ('dotted', 'Dotted')],
        default='solid')
    dataOffset = fields.Integer(string='Data Offset', default=0)
    cap = fields.Boolean(string='Cap', default=True)
    join = fields.Boolean(string='Join', default=True)
    minterLimit = fields.Integer(string='Minter Limit', default=0)
    shadowBlur = fields.Integer(string='Shadow Blur', default=0)
    shadowColor = fields.Char(string='Shadow Color', default='transparent')
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=0)
    opacity = fields.Float(string='Opacity', default=1)
