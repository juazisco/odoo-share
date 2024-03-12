# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsSeriersLine(models.Model):
    '''
    Mana Dashboard Text Style
    '''
    _name = 'mana_dashboard.echarts_series_line'

    type = fields.Char(string='Type', default='line')
    name = fields.Char(string='Name', default='')
    colorBy = fields.Char(string='Color By', default='series')
    coordinateSystem = fields.Char(string='Coordinate System', default='cartesian2d')
    xAxisIndex = fields.Char(string='X Axis Index', default='0')
    yAxisIndex = fields.Char(string='Y Axis Index', default='0')
    polarIndex = fields.Char(string='Polar Index', default='0')
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
    symbolOffset = fields.Char(string='Symbol Offset', default='[0, 0]')
    showSymbol = fields.Boolean(string='Show Symbol', default=True)
    showAllSymbol = fields.Boolean(string='Show All Symbol', default=False)
    hoverAnimation = fields.Boolean(string='Hover Animation', default=True)
    legendHoverLink = fields.Boolean(string='Legend Hover Link', default=True)
    stack = fields.Char(string='Stack', default='')
    stackStrategy = fields.Char(string='Stack Strategy', default='')
    cursor = fields.Char(string='Cursor', default='pointer')
    connectNulls = fields.Boolean(string='Connect Nulls', default=False)
    clip = fields.Boolean(string='Clip', default=True)
    triggerLineEvent = fields.Boolean(string='Trigger Line Event', default=False)
    step = fields.Boolean(string='Step', default=False)
    label = fields.Many2one(
        string='Label',
        comodel_name='mana_dashboard.echarts_label',
        ondelete='cascade')
    endLabel = fields.Many2one(
        string='End Label',
        comodel_name='mana_dashboard.echarts_label',
        ondelete='cascade')
    labelLine = fields.Many2one(
        string='Label Line',
        comodel_name='mana_dashboard.echarts_label_line',
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
    selectedMode = fields.Char(string='Selected Mode', default='false')
    smooth = fields.Boolean(string='Smooth', default=False)
    smoothMonotone = fields.Char(string='Smooth Monotone', default='')
    sampling = fields.Char(string='Sampling', default='')
    dimensions = fields.Char(string='Dimensions', default='')
    encode = fields.Char(string='Encode', default='')
    seriesLayoutBy = fields.Char(string='Series Layout By', default='column')
    datasetIndex = fields.Char(string='Dataset Index', default='0')
    dataGroupId = fields.Char(string='Data Group Id', default='')
    data = fields.Char(string='Data', default='')
    markPoint = fields.Many2one(
        string='Mark Point',
        comodel_name='mana_dashboard.echarts_mark_point',
        ondelete='cascade')
    markLine = fields.Many2one(
        string='Mark Line',
        comodel_name='mana_dashboard.echarts_mark_line',
        ondelete='cascade')
    markArea = fields.Many2one(
        string='Mark Area',
        comodel_name='mana_dashboard.echarts_mark_area',
        ondelete='cascade')
    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=2)
    silent = fields.Boolean(string='Silent', default=False)
    animation = fields.Boolean(string='Animation', default=True)
    animationThreshold = fields.Integer(string='Animation Threshold', default=2000)
    animationDuration = fields.Integer(string='Animation Duration', default=1000)
    animationEasing = fields.Char(string='Animation Easing', default='cubicOut')
    animationDelay = fields.Integer(string='Animation Delay', default=0)
    animationDurationUpdate = fields.Integer(string='Animation Duration Update', default=300)
    animationEasingUpdate = fields.Char(string='Animation Easing Update', default='cubicOut')
    animationDelayUpdate = fields.Integer(string='Animation Delay Update', default=0)
    universalTransition = fields.Many2one(
        string='Universal Transition',
        comodel_name='mana_dashboard.echarts_universal_transition',
        ondelete='cascade')
    tooltip = fields.Many2one(
        string='Tooltip',
        comodel_name='mana_dashboard.echarts_tooltip',
        ondelete='cascade')
