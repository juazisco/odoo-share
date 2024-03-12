# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsDataZoomInside(models.Model):
    '''
    Mana Dashboard Echarts Data Zoom Inside
    '''
    _name = 'mana_dashboard.echarts_data_zoom_inside'

    type = fields.Char(string='Type', default='inside')
    disabled = fields.Boolean(string='Disabled', default=False)
    xAxisIndex = fields.Integer(string='X Axis Index', default=0)
    yAxisIndex = fields.Integer(string='Y Axis Index', default=0)
    radfusAxisIndex = fields.Integer(string='Radfus Axis Index', default=0)
    angleAxisIndex = fields.Integer(string='Angle Axis Index', default=0)
    filterMode = fields.Selection(
        string='Filter Mode',
        selection=[
            ('filter', 'Filter'),
            ('empty', 'Empty'),
            ('weakFilter', 'Weak Filter'),
            ('none', 'None')
        ],
        default='filter'
    )
    start = fields.Integer(string='Start', default=0)
    end = fields.Integer(string='End', default=100)
    startValue = fields.Integer(string='Start Value', default=0)
    endValue = fields.Integer(string='End Value', default=100)
    minSpan = fields.Integer(string='Min Span', default=0)
    maxSpan = fields.Integer(string='Max Span', default=100)
    orient = fields.Selection(
        string='Orient',
        selection=[
            ('horizontal', 'Horizontal'),
            ('vertical', 'Vertical')
        ],
        default='horizontal'
    )
    zoomLock = fields.Boolean(string='Zoom Lock', default=False)
    throttle = fields.Integer(string='Throttle', default=100)
    rangeMode = fields.Selection(
        string='Range Mode',
        selection=[
            ('percent', 'Percent'),
            ('value', 'Value')
        ],
        default='percent'
    )
    zoomOnMouseWheel = fields.Boolean(string='Zoom On Mouse Wheel', default=True)
    moveOnMouseMove = fields.Boolean(string='Move On Mouse Move', default=True)
    moveOnMouseWheel = fields.Boolean(string='Move On Mouse Wheel', default=False)
    preventDefaultMouseMove = fields.Boolean(string='Prevent Default Mouse Move', default=False)


class EchartsDataZoomSlider(models.Model):
    '''
    Mana Dashboard Echarts Data Zoom Inside
    '''
    _name = 'mana_dashboard.echarts_data_zoom_slider'

    type = fields.Char(string='Type', default='slider')
    show = fields.Boolean(string='Show', default=True)
    backgroundColor = fields.Char(string='Background Color', default='rgba(47,69,84,0)')
    dataBackground = fields.Char(string='Data Background', default='#ddd')
    selectedDataBackground = fields.Char(string='Selected Data Background', default='#99c0dd')
    fillerColor = fields.Char(string='Filler Color', default='rgba(167,183,204,0.4)')
    borderColor = fields.Char(string='Border Color', default='#ddd')
    handleIcon = fields.Char(string='Handle Icon', default='M-9.7,0H9.7V2.9H-9.7z M-9.7,13.7H9.7V16.6H-9.7z M-4.8,6.8H4.8V9.7H-4.8z')
    handleSize = fields.Integer(string='Handle Size', default=20)
    handleStyle = fields.Many2one(
        string='Handle Style',
        comodel_name='mana_dashboard.echarts_data_zoom_slider_handle_style'
    )
    moveHandleIcon = fields.Char(string='Move Handle Icon', default='M-9.7,0H9.7V2.9H-9.7z M-9.7,13.7H9.7V16.6H-9.7z M-4.8,6.8H4.8V9.7H-4.8z')
    moveHandleSize = fields.Integer(string='Move Handle Size', default=20)
    moveHandleStyle = fields.Many2one(
        string='Move Handle Style',
        comodel_name='mana_dashboard.echarts_data_zoom_slider_move_handle_style'
    )
    labelPrecision = fields.Integer(string='Label Precision', default=2)
    labelFormatter = fields.Char(string='Label Formatter', default='{value}')
    showDetail = fields.Boolean(string='Show Detail', default=True)
    showDataShadow = fields.Selection(
        string='Show Data Shadow',
        selection=[
            ('auto', 'Auto'),
            ('true', 'True'),
            ('false', 'False')
        ],
        default='auto'
    )
    realtime = fields.Boolean(string='Realtime', default=True)
    textStyle = fields.Many2one(
        string='Text Style',
        comodel_name='mana_dashboard.echarts_data_zoom_slider_text_style'
    )
    xAxisIndex = fields.Integer(string='X Axis Index', default=0)
    yAxisIndex = fields.Integer(string='Y Axis Index', default=0)
    radfusAxisIndex = fields.Integer(string='Radfus Axis Index', default=0)
    angleAxisIndex = fields.Integer(string='Angle Axis Index', default=0)
    filterMode = fields.Selection(
        string='Filter Mode',
        selection=[
            ('filter', 'Filter'),
            ('empty', 'Empty'),
            ('weakFilter', 'Weak Filter'),
            ('none', 'None')
        ],
        default='filter'
    )
    start = fields.Integer(string='Start', default=0)
    end = fields.Integer(string='End', default=100)
    startValue = fields.Integer(string='Start Value', default=0)
    endValue = fields.Integer(string='End Value', default=100)
    minSpan = fields.Integer(string='Min Span', default=0)
    maxSpan = fields.Integer(string='Max Span', default=100)
    orient = fields.Selection(
        string='Orient',
        selection=[
            ('horizontal', 'Horizontal'),
            ('vertical', 'Vertical')
        ],
        default='horizontal'
    )
    zoomLock = fields.Boolean(string='Zoom Lock', default=False)
    throttle = fields.Integer(string='Throttle', default=100)
    rangeMode = fields.Selection(
        string='Range Mode',
        selection=[
            ('percent', 'Percent'),
            ('value', 'Value')
        ],
        default='percent'
    )
    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=4)
    left = fields.Char(string='Left', default='auto')
    top = fields.Char(string='Top', default='auto')
    right = fields.Char(string='Right', default='auto')
    bottom = fields.Char(string='Bottom', default='auto')
    width = fields.Char(string='Width', default='auto')
    height = fields.Char(string='Height', default='auto')
    brushSelect = fields.Boolean(string='Brush Select', default=False)
    brushStyle = fields.Many2one(
        string='Brush Style',
        comodel_name='mana_dashboard.echarts_data_zoom_slider_brush_style'
    )
    emphasis = fields.Many2one(
        string='Emphasis',
        comodel_name='mana_dashboard.echarts_data_zoom_slider_emphasis'
    )
