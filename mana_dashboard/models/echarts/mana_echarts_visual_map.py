# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsVisualMap(models.Model):
    '''
    Mana Dashboard Echarts Visual Map
    '''
    _name = 'mana_dashboard.echarts_visual_map'

    type = fields.Selection(
        string='Type',
        selection=[
            ('continuous', 'Continuous'),
            ('piecewise', 'Piecewise')],
        default='continuous')
    range = fields.Char(string='Range', default='[0, 100]')
    min = fields.Integer(string='Min', default=0)
    max = fields.Integer(string='Max', default=100)
    calculable = fields.Boolean(string='Calculable', default=True)
    realtime = fields.Boolean(string='Realtime', default=True)
    inverse = fields.Boolean(string='Inverse', default=False)
    precision = fields.Integer(string='Precision', default=0)
    itemWidth = fields.Integer(string='Item Width', default=20)
    itemHeight = fields.Integer(string='Item Height', default=14)
    align = fields.Selection(
        string='Align',
        selection=[
            ('auto', 'Auto'),
            ('left', 'Left'),
            ('right', 'Right')],
        default='auto')
    text = fields.List(string='Text', default=[])
    textGap = fields.Integer(string='Text Gap', default=10)
    show = fields.Boolean(string='Show', default=True)
    dimension = fields.Integer(string='Dimension', default=0)
    seriesIndex = fields.Integer(string='Series Index', default=0)
    hoverLink = fields.Boolean(string='Hover Link', default=True)
    inRange = fields.Many2one(
        string='In Range',
        comodel_name='mana_dashboard.echarts_visual_map_in_range',
        ondelete='cascade')
    outOfRange = fields.Many2one(
        string='Out Of Range',
        comodel_name='mana_dashboard.echarts_visual_map_out_of_range',
        ondelete='cascade')
    controller = fields.Many2one(
        string='Controller',
        comodel_name='mana_dashboard.echarts_visual_map_controller',
        ondelete='cascade')
    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=4)
    left = fields.Char(string='Left', default='auto')
    top = fields.Char(string='Top', default='auto')
    right = fields.Char(string='Right', default='auto')
    bottom = fields.Char(string='Bottom', default='auto')
    orient = fields.Selection(
        string='Orient',
        selection=[
            ('horizontal', 'Horizontal'),
            ('vertical', 'Vertical')],
        default='vertical')
    padding = fields.Integer(string='Padding', default=5)
    backgroundColor = fields.Char(string='Background Color', default='rgba(0, 0, 0, 0)')
    borderColor = fields.Char(string='Border Color', default='#ccc')
    borderWidth = fields.Integer(string='Border Width', default=0)
    color = fields.Char(string='Color', default=['#bf444c', '#d88273', '#f6efa6'])
    textStyle = fields.Many2one(
        string='Text Style',
        comodel_name='mana_dashboard.echarts_text_style',
        ondelete='cascade')
    formatter = fields.Char(string='Formatter', default='{value}')
    handleIcon = fields.Char(string='Handle Icon', default='path://M-10.0,0.0 L-5.0,5.0 L-5.0,-5.0 L-10.0,0.0 Z M10.0,0.0 L5.0,5.0 L5.0,-5.0 L10.0,0.0 Z')
    handleSize = fields.Integer(string='Handle Size', default=45)
    handleStyle = fields.Many2one(
        string='Handle Style',
        comodel_name='mana_dashboard.echarts_visual_map_handle_style',
        ondelete='cascade')
    indicatorIcon = fields.Char(string='Indicator Icon', default='circle')
    indicatorSize = fields.Integer(string='Indicator Size', default=15)
    indicatorStyle = fields.Many2one(
        string='Indicator Style',
        comodel_name='mana_dashboard.echarts_visual_map_indicator_style',
        ondelete='cascade')
