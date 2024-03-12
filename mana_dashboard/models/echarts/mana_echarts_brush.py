# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsBrush(models.Model):
    '''
    Mana Dashboard Echarts Brush
    '''
    _name = 'mana_dashboard.echarts_brush'

    toolbox = fields.Selection(
        string='Toolbox',
        selection=[
            ('none', 'None'),
            ('rect', 'Rect'),
            ('polygon', 'Polygon'),
            ('lineX', 'Line X'),
            ('lineY', 'Line Y'),
            ('keep', 'Keep'),
            ('clear', 'Clear')],
        default='none')
    brushLink = fields.Char(string='Brush Link', default='')
    seriesIndex = fields.Char(string='Series Index', default='')
    geoIndex = fields.Char(string='Geo Index', default='')
    xAxisIndex = fields.Char(string='X Axis Index', default='')
    yAxisIndex = fields.Char(string='Y Axis Index', default='')
    brushType = fields.Selection(
        string='Brush Type',
        selection=[
            ('rect', 'Rect'),
            ('polygon', 'Polygon'),
            ('lineX', 'Line X'),
            ('lineY', 'Line Y'),
            ('keep', 'Keep'),
            ('clear', 'Clear')],
        default='rect')
    brushMode = fields.Selection(
        string='Brush Mode',
        selection=[
            ('single', 'Single'),
            ('multiple', 'Multiple')],
        default='single')
    transformable = fields.Boolean(string='Transformable', default=True)
    brushStyle = fields.Many2one(
        string='Brush Style',
        comodel_name='mana_dashboard.echarts_item_style',
        ondelete='cascade')
    throttleType = fields.Selection(
        string='Throttle Type',
        selection=[
            ('debounce', 'Debounce'),
            ('fixRate', 'Fix Rate')],
        default='debounce')
    throttleDelay = fields.Integer(string='Throttle Delay', default=0)
    removeOnClick = fields.Boolean(string='Remove On Click', default=True)
    inBrush = fields.Selection(
        string='In Brush',
        selection=[
            ('symbol', 'Symbol'),
            ('symbolSize', 'Symbol Size'),
            ('color', 'Color'),
            ('colorAlpha', 'Color Alpha'),
            ('opacity', 'Opacity'),
            ('colorLightness', 'Color Lightness'),
            ('colorSaturation', 'Color Saturation'),
            ('colorHue', 'Color Hue')],
        default='colorAlpha')
    outOfBrush = fields.Selection(
        string='Out Of Brush',
        selection=[
            ('symbol', 'Symbol'),
            ('symbolSize', 'Symbol Size'),
            ('color', 'Color'),
            ('colorAlpha', 'Color Alpha'),
            ('opacity', 'Opacity'),
            ('colorLightness', 'Color Lightness'),
            ('colorSaturation', 'Color Saturation'),
            ('colorHue', 'Color Hue')],
        default='colorAlpha')
    z = fields.Integer(string='Z', default=10000)
