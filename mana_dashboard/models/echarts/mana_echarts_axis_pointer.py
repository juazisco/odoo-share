# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsAxisPointer(models.Model):
    '''
    Mana Dashboard Echarts Visual Map
    '''
    _name = 'mana_dashboard.echarts_axis_pointer'

    show = fields.Boolean(string='Show', default=True)
    type = fields.Selection(
        string='Type',
        selection=[
            ('line', 'Line'),
            ('shadow', 'Shadow'),
            ('cross', 'Cross'),
            ('none', 'None')],
        default='line')
    snap = fields.Boolean(string='Snap', default=False)
    z = fields.Integer(string='Z', default=0)
    label = fields.Many2one(
        string='Label',
        comodel_name='mana_dashboard.echarts_axis_pointer_label',
        ondelete='cascade')
    lineStyle = fields.Many2one(
        string='Line Style',
        comodel_name='mana_dashboard.echarts_axis_pointer_line_style',
        ondelete='cascade')
    shadowStyle = fields.Many2one(
        string='Shadow Style',
        comodel_name='mana_dashboard.echarts_axis_pointer_shadow_style',
        ondelete='cascade')
    triggerEmphasis = fields.Many2one(
        string='Trigger Emphasis',
        comodel_name='mana_dashboard.echarts_axis_pointer_trigger_emphasis',
        ondelete='cascade')
    triggerTooltip = fields.Many2one(
        string='Trigger Tooltip',
        comodel_name='mana_dashboard.echarts_axis_pointer_trigger_tooltip',
        ondelete='cascade')
    value = fields.Integer(string='Value', default=0)
    status = fields.Boolean(string='Status', default=True)
    handle = fields.Many2one(
        string='Handle',
        comodel_name='mana_dashboard.echarts_axis_pointer_handle',
        ondelete='cascade')
    link = fields.List(string='Link', default=[])
    triggerOn = fields.Selection(
        string='Trigger On',
        selection=[
            ('mousemove', 'Mousemove'),
            ('click', 'Click'),
            ('none', 'None')],
        default='mousemove')
