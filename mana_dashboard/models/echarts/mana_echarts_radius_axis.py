# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsRadiusAxis(models.Model):
    '''
    Mana Dashboard Echarts Title
    '''
    _name = 'mana_dashboard.echarts_radius_axis'

    polarIndex = fields.Integer(string='Polar Index', default=0)
    type = fields.Char(string='Type', default='value')
    name = fields.Char(string='Name', default='')
    nameLocation = fields.Char(string='Name Location', default='end')
    nameTextStyle = fields.Many2one(
        string='Name Text Style',
        comodel_name='mana_dashboard.echarts_text_style',
        ondelete='cascade')
    nameGap = fields.Integer(string='Name Gap', default=15)
    nameRotate = fields.Integer(string='Name Rotate', default=0)
    inverse = fields.Boolean(string='Inverse', default=False)
    boundaryGap = fields.Boolean(string='Boundary Gap', default=True)
    min = fields.Integer(string='Min', default=0)
    max = fields.Integer(string='Max', default=100)
    scale = fields.Boolean(string='Scale', default=False)
    splitNumber = fields.Integer(string='Split Number', default=5)
    minInterval = fields.Integer(string='Min Interval', default=0)
    interval = fields.Integer(string='Interval', default=0)
    logBase = fields.Integer(string='Log Base', default=10)
    silent = fields.Boolean(string='Silent', default=False)
    triggerEvent = fields.Boolean(string='Trigger Event', default=False)
