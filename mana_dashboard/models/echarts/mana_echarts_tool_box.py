# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsToolBox(models.Model):
    '''
    Mana Dashboard Echarts Tool Box
    '''
    _name = 'mana_dashboard.echarts_tool_box'

    show = fields.Boolean(string='Show', default=True)
    orient = fields.Selection(
        string='Orient',
        selection=[
            ('horizontal', 'Horizontal'),
            ('vertical', 'Vertical')],
        default='horizontal')
    itemSize = fields.Integer(string='Item Size', default=15)
    itemGap = fields.Integer(string='Item Gap', default=10)
    showTitle = fields.Boolean(string='Show Title', default=True)
    feature = fields.Many2one(
        string='Feature',
        comodel_name='mana_dashboard.echarts_feature',
        ondelete='restrict')
    iconStyle = fields.Many2one(
        string='Icon Style',
        comodel_name='mana_dashboard.echarts_icon_style',
        ondelete='restrict')
    emphasis = fields.Many2one(
        string='Emphasis',
        comodel_name='mana_dashboard.echarts_emphasis',
        ondelete='restrict')
    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=6)
    left = fields.Char(string='Left', default='auto')
    top = fields.Char(string='Top', default='auto')
    right = fields.Char(string='Right', default='auto')
    bottom = fields.Char(string='Bottom', default='auto')
    width = fields.Char(string='Width', default='auto')
    height = fields.Char(string='Height', default='auto')
    tooltip = fields.Many2one(
        string='Tooltip',
        comodel_name='mana_dashboard.echarts_tooltip',
        ondelete='restrict')
