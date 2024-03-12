# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsRadar(models.Model):
    '''
    Mana Dashboard Echarts Title
    '''
    _name = 'mana_dashboard.echarts_radar'

    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=2)
    center = fields.Char(string='Center', default='center')
    radius = fields.Char(string='Radius', default='75%')
    startAngle = fields.Integer(string='Start Angle', default=90)
    axisNname = fields.Many2one(
        string='Axis Name',
        comodel_name='mana_dashboard.echarts_axis_name',
        ondelete='cascade')
    nameGap = fields.Integer(string='Name Gap', default=15)
    splitNumber = fields.Integer(string='Split Number', default=5)
    shape = fields.Selection(
        string='Shape',
        selection=[
            ('polygon', 'Polygon'),
            ('circle', 'Circle')],
        default='polygon')
    scale = fields.Boolean(string='Scale', default=False)
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
    indicator = fields.Many2Many(
        string='Indicator',
        comodel_name='mana_dashboard.echarts_indicator',
        relation='mana_dashboard_echarts_radar_indicator_rel',
        column1='radar_id',
        column2='indicator_id')
