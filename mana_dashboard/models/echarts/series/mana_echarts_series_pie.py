# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsSeriersPie(models.Model):
    '''
    Mana Dashboard Text Style
    '''
    _name = 'mana_dashboard.echarts_series_pie'

    type = fields.Char(string='Type', default='pie')
    name = fields.Char(string='Name', default='')
    colorBy = fields.Char(string='Color By', default='series')
    legendHoverLink = fields.Boolean(string='Legend Hover Link', default=True)
    coordinateSystem = fields.Char(string='Coordinate System', default='cartesian2d')
    geoIndex = fields.Char(string='Geo Index', default='0')
    calendarIndex = fields.Char(string='Calendar Index', default='0')
    selectedMode = fields.Char(string='Selected Mode', default='false')
    selectedOffset = fields.Integer(string='Selected Offset', default=10)
    clockwise = fields.Boolean(string='Clockwise', default=True)
    startAngle = fields.Integer(string='Start Angle', default=90)
    minAngle = fields.Integer(string='Min Angle', default=0)
    minShowLabelAngle = fields.Integer(string='Min Show Label Angle', default=0)
    roseType = fields.Selection(
        string='Rose Type',
        selection=[
            ('radius', 'Radius'),
            ('area', 'Area')
        ],
        default='radius')
    avoidLabelOverlap = fields.Boolean(string='Avoid Label Overlap', default=True)
    stillShowZeroSum = fields.Boolean(string='Still Show Zero Sum', default=True)
    percentPrecision = fields.Integer(string='Percent Precision', default=2)
    cursor = fields.Char(string='Cursor', default='pointer')
    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=2)
    left = fields.Char(string='Left', default='center')
    top = fields.Char(string='Top', default='middle')
    right = fields.Char(string='Right', default='auto')
    bottom = fields.Char(string='Bottom', default='auto')
    width = fields.Char(string='Width', default='auto')
    height = fields.Char(string='Height', default='auto')
    showEmptyCircle = fields.Boolean(string='Show Empty Circle', default=True)
    emptyCircleStyle = fields.Many2one(
        string='Empty Circle Style',
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
    select = fields.Many2one(
        string='Select',
        comodel_name='mana_dashboard.echarts_select',
        ondelete='cascade')
    center = fields.Char(string='Center', default='center')
    radius = fields.Char(string='Radius', default='[0, \'75%\']')
    seriesLayoutBy = fields.Char(string='Series Layout By', default='column')
    datasetIndex = fields.Char(string='Dataset Index', default='0')
    dimensions = fields.Char(string='Dimensions', default='auto')
    encode = fields.Char(string='Encode', default='auto')
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
    silent = fields.Boolean(string='Silent', default=False)
    animationType = fields.Char(string='Animation Type', default='expansion')
    animationTypeUpdate = fields.Char(string='Animation Type Update', default='transition')
    animation = fields.Boolean(string='Animation', default=True)
    animationThreshold = fields.Integer(string='Animation Threshold', default=2000)
    animationDuration = fields.Integer(string='Animation Duration', default=1000)
    animationEasing = fields.Char(string='Animation Easing', default='cubicOut')
    animationDelay = fields.Char(string='Animation Delay', default='0')
    animationDurationUpdate = fields.Integer(string='Animation Duration Update', default=300)
    animationEasingUpdate = fields.Char(string='Animation Easing Update', default='cubicOut')
    animationDelayUpdate = fields.Char(string='Animation Delay Update', default='0')
    universalTransition = fields.Many2one(
        string='Universal Transition',
        comodel_name='mana_dashboard.echarts_universal_transition',
        ondelete='cascade')
    tooltip = fields.Many2one(
        string='Tooltip',
        comodel_name='mana_dashboard.echarts_tooltip',
        ondelete='cascade')
