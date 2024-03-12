# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsToolTip(models.Model):
    '''
    Mana Dashboard Echarts Title
    '''
    _name = 'mana_dashboard.echarts_tooltip'

    show = fields.Boolean(string='Show', default=True)
    trigger = fields.Selection(
        string='Trigger',
        selection=[
            ('item', 'Item'),
            ('axis', 'Axis'),
            ('none', 'None')],
        default='item')
    
    axisPointer = fields.Many2one(
        string='Axis Pointer',
        comodel_name='mana_dashboard.axis_pointer',
        ondelete='cascade')
    
    showContent = fields.Boolean(string='Show Content', default=True)
    alwaysShowContent = fields.Boolean(string='Always Show Content', default=False)
    triggerOn = fields.Selection(
        string='Trigger On',
        selection=[
            ('mousemove', 'Mouse Move'),
            ('click', 'Click'),
            ('mousemove|click', 'Mouse Move & Click'),
            ('none', 'None')],
        default='mousemove|click')
    
    showDelay = fields.Integer(string='Show Delay', default=0)
    hideDelay = fields.Integer(string='Hide Delay', default=100)
    enterable = fields.Boolean(string='Enterable', default=False)
    confine = fields.Boolean(string='Confine', default=False)
    appendToBody = fields.Boolean(string='Append To Body', default=False)
    className = fields.Char(string='Class Name', default='')
    transitionDuration = fields.Integer(string='Transition Duration', default=0)
    position = fields.Char(string='Position', default='right')
    formatter = fields.Char(string='Formatter', default='{a} <br/>{b} : {c}')
    valueFormatter = fields.Char(string='Value Formatter', default='')
    backgroundColor = fields.Char(string='Background Color', default='rgba(50,50,50,0.7)')
    borderColor = fields.Char(string='Border Color', default='#333')
    borderWidth = fields.Integer(string='Border Width', default=0)
    padding = fields.Char(string='Padding', default='5')
    textStyle = fields.Many2one(
        string='Text Style',
        comodel_name='mana_dashboard.text_style',
        ondelete='cascade')
    extraCssText = fields.Char(string='Extra CSS Text', default='')
    order = fields.Char(string='Order', default='null')
