# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsSeriersRadar(models.Model):
    '''
    Mana Dashboard Series Radar
    '''
    _name = 'mana_dashboard.echarts_series_radar'

    type = fields.Char(string='Type', default='radar')
    name = fields.Char(string='Name', default='')
    colorBy = fields.Char(string='Color By', default='series')
    coordinateSystem = fields.Char(string='Coordinate System', default='radar')
    radarIndex = fields.Char(string='Radar Index', default='0')
    symbol = fields.Selection(
        string='Symbol',
        selection=[
            ('none', 'None'),
            ('circle', 'Circle'),
            ('rect', 'Rect'),
            ('roundRect', 'Round Rect'),
            ('triangle', 'Triangle'),
            ('diamond', 'Diamond'),
            ('pin', 'Pin'),
            ('arrow', 'Arrow')],
        default='none')
    symbolSize = fields.Integer(string='Symbol Size', default=4)
    symbolRotate = fields.Integer(string='Symbol Rotate', default=0)
    symbolKeepAspect = fields.Boolean(string='Symbol Keep Aspect', default=False)
    symbolOffset = fields.Char(string='Symbol Offset', default='[0, 0]')
    label = fields.Many2one(
        string='Label',
        comodel_name='mana_dashboard.echarts_label',
        ondelete='cascade')
    labelLayout = fields.Char(string='Label Layout', default='')
    itemStyle = fields.Many2one(
        string='Item Style',
        comodel_name='mana_dashboard.echarts_item_style',
        ondelete='cascade')
    lineStyle = fields.Many2one(
        string='Line Style',
        comodel_name='mana_dashboard.echarts_line_style',
        ondelete='cascade')
    areaStyle = fields.Many2one(
        string='Area Style',
        comodel_name='mana_dashboard.echarts_area_style',
        ondelete='cascade')
    emphasis = fields.Many2one(
        string='Emphasis',
        comodel_name='mana_dashboard.echarts_emphasis',
        ondelete='cascade')
    blur = fields.Many2one(
        string='Blur',
        comodel_name='mana_dashboard.echarts_blur',
        ondelete='cascade')
    select = fields.Many2one(
        string='Select',
        comodel_name='mana_dashboard.echarts_select',
        ondelete='cascade')
    selctedMode = fields.Char(string='Selected Mode', default='false')
    dataGroupId = fields.Char(string='Data Group Id', default='')
    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=2)
    silent = fields.Boolean(string='Silent', default=False)
    animation = fields.Boolean(string='Animation', default=True)
    animationThreshold = fields.Integer(string='Animation Threshold', default=2000)
    animationDuration = fields.Integer(string='Animation Duration', default=1000)
    animationEasing = fields.Char(string='Animation Easing', default='linear')
    animationDelay = fields.Char(string='Animation Delay', default='0')
    animationDurationUpdate = fields.Integer(string='Animation Duration Update', default=300)
    animationEasingUpdate = fields.Char(string='Animation Easing Update', default='cubicOut')
    universalTransition = fields.Boolean(string='Universal Transition', default=True)
    tooltip = fields.Many2one(
        string='Tooltip',
        comodel_name='mana_dashboard.echarts_tooltip',
        ondelete='cascade')

