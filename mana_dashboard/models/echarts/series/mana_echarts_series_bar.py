# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsSeriersBar(models.Model):
    '''
    Mana Dashboard Series Bar
    '''
    _name = 'mana_dashboard.echarts_series_bar'

    type = fields.Char(string='Type', default='line')
    name = fields.Char(string='Name', default='')
    colorBy = fields.Char(string='Color By', default='series')
    coordinateSystem = fields.Char(string='Coordinate System', default='cartesian2d')
    xAxisIndex = fields.Char(string='X Axis Index', default='0')
    yAxisIndex = fields.Char(string='Y Axis Index', default='0')
    polarIndex = fields.Char(string='Polar Index', default='0')
    roundCap = fields.Boolean(string='Round Cap', default=False)
    realtimeSort = fields.Boolean(string='Realtime Sort', default=False)
    showBackground = fields.Boolean(string='Show Background', default=False)
    backgroundStyle = fields.Many2one(
        string='Background Style',
        comodel_name='mana_dashboard.echarts_item_style',
        ondelete='cascade')
    label = fields.Many2one(
        string='Label',
        comodel_name='mana_dashboard.echarts_label',
        ondelete='cascade')
    labelLine = fields.Many2one(
        string='Label Line',
        comodel_name='mana_dashboard.echarts_label_line',
        ondelete='cascade')
    itemStyle = fields.Many2one(
        string='Item Style',
        comodel_name='mana_dashboard.echarts_item_style',
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
    stack = fields.Char(string='Stack', default='')
    stackStrategy = fields.Char(string='Stack Strategy', default='')
    sampling = fields.Selection(
        string='Sampling',
        selection=[
            ('lttb', 'Lttb'),
            ('min', 'Min'),
            ('max', 'Max'),
            ('average', 'Average')
        ],
        default='lttb')
    cursor = fields.Char(string='Cursor', default='pointer')
    barWidth = fields.Char(string='Bar Width', default='auto')
    barMaxWidth = fields.Char(string='Bar Max Width', default='auto')
    barMinHeight = fields.Integer(string='Bar Min Height', default=0)
    barGap = fields.Char(string='Bar Gap', default='30%')
    barCategoryGap = fields.Char(string='Bar Category Gap', default='20%')
    large = fields.Boolean(string='Large', default=False)
    largeThreshold = fields.Integer(string='Large Threshold', default=400)
    progressive = fields.Integer(string='Progressive', default=400)
    progressiveThreshold = fields.Integer(string='Progressive Threshold', default=3000)
    progressiveChunkMode = fields.Char(string='Progressive Chunk Mode', default='mod')
    dimensions = fields.Char(string='Dimensions', default='auto')
    encode = fields.Char(string='Encode', default='auto')
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
    slient = fields.Boolean(string='Slient', default=False)
    animation = fields.Boolean(string='Animation', default=True)
    animationThreshold = fields.Integer(string='Animation Threshold', default=2000)
    animationDuration = fields.Integer(string='Animation Duration', default=1000)
    animationEasing = fields.Char(string='Animation Easing', default='cubicOut')
    animationDelay = fields.Char(string='Animation Delay', default='0')
    animationDurationUpdate = fields.Integer(string='Animation Duration Update', default=300)
    animationEasingUpdate = fields.Char(string='Animation Easing Update', default='cubicOut')
    animationDelayUpdate = fields.Char(string='Animation Delay Update', default='0')
    universalTransition = fields.Char(string='Universal Transition', default='true')
    tooltip = fields.Many2one(
        string='Tooltip',
        comodel_name='mana_dashboard.echarts_tooltip',
        ondelete='cascade')
