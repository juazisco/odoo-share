# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsSeriersGuage(models.Model):
    '''
    Mana Dashboard Gauge
    '''
    _name = 'mana_dashboard.echarts_series_gauge'

    type = fields.Char(string='Type', default='gauge')
    name = fields.Char(string='Name', default='')
    colorBy = fields.Char(string='Color By', default='series')
    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=2)
    center = fields.Char(string='Center', default='["50%", "50%"]')
    radius = fields.Char(string='Radius', default='75%')
    legendHoverLink = fields.Boolean(string='Legend Hover Link', default=True)
    startAngle = fields.Integer(string='Start Angle', default=225)
    endAngle = fields.Integer(string='End Angle', default=-45)
    clockwise = fields.Boolean(string='Clockwise', default=True)
    min = fields.Integer(string='Min', default=0)
    max = fields.Integer(string='Max', default=100)
    splitNumber = fields.Integer(string='Split Number', default=10)
    axisLine = fields.Many2one(
        string='Axis Line',
        comodel_name='mana_dashboard.echarts_axis_line',
        ondelete='cascade')
    splitLine = fields.Many2one(
        string='Split Line',
        comodel_name='mana_dashboard.echarts_split_line',
        ondelete='cascade')
    axisTick = fields.Many2one(
        string='Axis Tick',
        comodel_name='mana_dashboard.echarts_axis_tick',
        ondelete='cascade')
    axisLabel = fields.Many2one(
        string='Axis Label',
        comodel_name='mana_dashboard.echarts_axis_label',
        ondelete='cascade')
    pointer = fields.Many2one(
        string='Pointer',
        comodel_name='mana_dashboard.echarts_pointer',
        ondelete='cascade')
    anchor = fields.Many2one(
        string='Anchor',
        comodel_name='mana_dashboard.echarts_anchor',
        ondelete='cascade')
    itemStyle = fields.Many2one(
        string='Item Style',
        comodel_name='mana_dashboard.echarts_item_style',
        ondelete='cascade')
    emphasis = fields.Many2one(
        string='Emphasis',
        comodel_name='mana_dashboard.echarts_emphasis',
        ondelete='cascade')
    title = fields.Many2one(
        string='Title',
        comodel_name='mana_dashboard.echarts_title',
        ondelete='cascade')
    detail = fields.Many2one(
        string='Detail',
        comodel_name='mana_dashboard.echarts_detail',
        ondelete='cascade')
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
    slient = fields.Boolean(string='Slient', default=False)
    animation = fields.Boolean(string='Animation', default=True)
    animationThreshold = fields.Integer(string='Animation Threshold', default=2000)
    animationDuration = fields.Integer(string='Animation Duration', default=1000)
    animationEasing = fields.Char(string='Animation Easing', default='cubicOut')
    animationDurationUpdate = fields.Integer(string='Animation Duration Update', default=300)
    animationEasingUpdate = fields.Char(string='Animation Easing Update', default='cubicOut')
    animationDelay = fields.Char(string='Animation Delay', default='0')
    animationDelayUpdate = fields.Char(string='Animation Delay Update', default='0')
    tooltip = fields.Many2one(
        string='Tooltip',
        comodel_name='mana_dashboard.echarts_tooltip',
        ondelete='cascade')

    
  