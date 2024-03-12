# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsAngleAxis(models.Model):
    '''
    Mana Dashboard Echarts Title
    '''
    _name = 'mana_dashboard.echarts_angle_axis'

    polarIndex = fields.Integer(string='Polar Index', default=0)
    startAngle = fields.Integer(string='Start Angle', default=90)
    clockwise = fields.Boolean(string='Clockwise', default=True)
    type = fields.Char(string='Type', default='value')
    boundaryGap = fields.Boolean(string='Boundary Gap', default=True)
    min = fields.Integer(string='Min', default=0)
    max = fields.Integer(string='Max', default=100)
    scale = fields.Boolean(string='Scale', default=False)
    splitNumber = fields.Integer(string='Split Number', default=5)
    minInterval = fields.Integer(string='Min Interval', default=0)
    maxInterval = fields.Integer(string='Max Interval', default=0)
    interval = fields.Integer(string='Interval', default=0)
    logBase = fields.Integer(string='Log Base', default=10)
    silent = fields.Boolean(string='Silent', default=False)
    triggerEvent = fields.Boolean(string='Trigger Event', default=False)
    axisLine = fields.Many2one(
        string='Axis Line',
        comodel_name='mana_dashboard.echarts_axis_line',
        ondelete='cascade')
    axisTick = fields.Many2one(
        string='Axis Tick',
        comodel_name='mana_dashboard.echarts_axis_tick',
        ondelete='cascade')
    axisLabel = fields.Many2one(
        string='Axis Label',
        comodel_name='mana_dashboard.echarts_axis_label',
        ondelete='cascade')
    splitLine = fields.Many2one(
        string='Split Line',
        comodel_name='mana_dashboard.echarts_split_line',
        ondelete='cascade')
    splitArea = fields.Many2one(
        string='Split Area',
        comodel_name='mana_dashboard.echarts_split_area',
        ondelete='cascade')
    data = fields.Char(string='Data', default='[]')
    axisPointer = fields.Many2one(
        string='Axis Pointer',
        comodel_name='mana_dashboard.echarts_axis_pointer',
        ondelete='cascade')
    animation = fields.Boolean(string='Animation', default=True)
    animationThreshold = fields.Integer(
        string='Animation Threshold', default=2000)
    animationDuration = fields.Integer(string='Animation Duration', default=1000)
    animationEasing = fields.Char(string='Animation Easing', default='cubicOut')
    animationDelay = fields.Integer(string='Animation Delay', default=0)
    animationDurationUpdate = fields.Integer(
        string='Animation Duration Update', default=300)
    animationEasingUpdate = fields.Char(
        string='Animation Easing Update', default='cubicOut')
    animationDelayUpdate = fields.Integer(
        string='Animation Delay Update', default=0)
    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=2)
