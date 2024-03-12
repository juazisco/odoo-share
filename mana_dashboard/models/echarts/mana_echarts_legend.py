# -*- coding: utf-8 -*-

from odoo import models, fields, _


class Legend(models.Model):
    '''
    Mana Dashboard Text Style
    '''
    _name = 'mana_dashboard.legend'

    show = fields.Boolean(string='Show', default=True)
    type = fields.Selection(
        string='Type',
        selection=[
            ('plain', 'Plain'),
            ('scroll', 'Scroll')],
        default='plain')
    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=4)
    left = fields.Char(string='Left', default='auto')
    top = fields.Char(string='Top', default='auto')
    right = fields.Char(string='Right', default='auto')
    bottom = fields.Char(string='Bottom', default='auto')
    width = fields.Char(string='Width', default='auto')
    height = fields.Char(string='Height', default='auto')
    orient = fields.Selection(
        string='Orient',
        selection=[
            ('horizontal', 'Horizontal'),
            ('vertical', 'Vertical')],
        default='horizontal')
    align = fields.Selection(
        string='Align',
        selection=[
            ('auto', 'Auto'),
            ('left', 'Left'),
            ('right', 'Right')],
        default='auto')
    padding = fields.Char(string='Padding', default='5')
    itemGap = fields.Integer(string='Item Gap', default=10)
    itemWidth = fields.Integer(string='Item Width', default=25)
    itemHeight = fields.Integer(string='Item Height', default=14)
    
    itemStyle = fields.Many2one(
        string='Item Style',
        comodel_name='mana_dashboard.text_style',
        ondelete='cascade')
    
    lineStyle = fields.Many2one(
        string='Line Style',
        comodel_name='mana_dashboard.line_style',
        ondelete='cascade')
    
    symbolRotate = fields.Integer(string='Symbol Rotate', default=0)
    formatter = fields.Char(string='Formatter', default='{name}')
    selectedMode = fields.Selection(
        string='Selected Mode',
        selection=[
            ('true', 'True'),
            ('false', 'False'),
            ('single', 'Single'),
            ('multiple', 'Multiple')],
        default='true')
    inactiveColor = fields.Char(string='Inactive Color', default='#ccc')
    # need optimize
    selected = fields.Char(string='Selected', default='') 
    textStyle = fields.Many2one(
        string='Text Style',
        comodel_name='mana_dashboard.text_style',
        ondelete='cascade')
    
    tooltip = fields.Many2one(
        string='Tooltip',
        comodel_name='mana_dashboard.tooltip',
        ondelete='cascade')
    
    icon_type = fields.Selection(
        string='Icon Type',
        selection=[
            ('circle', 'Circle'),
            ('rect', 'Rect'),
            ('roundRect', 'Round Rect'),
            ('triangle', 'Triangle'),
            ('diamond', 'Diamond'),
            ('pin', 'Pin'),
            ('arrow', 'Arrow'),
            ('custom', 'Custom')],
        default='rect')
    
    custom_icon = fields.Char(string='Custom Icon', default='')
    backgroundColor = fields.Char(string='Background Color', default='transparent')
    borderColor = fields.Char(string='Border Color', default='#ccc')
    borderWidth = fields.Integer(string='Border Width', default=0)
    borderRadius = fields.Integer(string='Border Radius', default=0)    
    shadowBlur = fields.Integer(string='Shadow Blur', default=0)
    shadowColor = fields.Char(string='Shadow Color', default='transparent')
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=0)
    pageButtonItemGap = fields.Integer(string='Page Button Item Gap', default=5)
    pageButtonGap = fields.Integer(string='Page Button Gap', default=5)
    pageButtonPosition = fields.Selection(
        string='Page Button Position',
        selection=[
            ('start', 'Start'),
            ('end', 'End')],
        default='end')
    pageFormatter = fields.Char(string='Page Formatter', default='{current}/{total}')
    pageIcons_horizontal = fields.Char(string='Page Icons Horizontal', default='M0,0L12,-10L12,10z')
    pageIcons_vertical = fields.Char(string='Page Icons Vertical', default='M0,0L-12,-10L-12,10z')
    pageIconColor = fields.Char(string='Page Icon Color', default='#2f4554')
    pageIconInactiveColor = fields.Char(string='Page Icon Inactive Color', default='#aaa')
    pageIconSize = fields.Integer(string='Page Icon Size', default=15)
    pageTextStyle = fields.Many2one(
        string='Page Text Style',
        comodel_name='mana_dashboard.text_style',
        ondelete='cascade')
    animation = fields.Boolean(string='Animation', default=True)
    animationDurationUpdate = fields.Integer(string='Animation Duration Update', default=800)
    animationEasingUpdate = fields.Char(string='Animation Easing Update', default='cubicOut')
    enphasis = fields.Many2one(
        string='Enphasis',
        comodel_name='mana_dashboard.enphasis',
        ondelete='cascade')
    selector = fields.Boolean(string='Selector', default=False)
    selectorLabel = fields.Many2one(
        string='Selector Label',
        comodel_name='mana_dashboard.echarts_selector_label',
        ondelete='cascade')
    selectorPosition = fields.Selection(
        string='Selector Position',
        selection=[
            ('auto', 'Auto'),
            ('start', 'Start'),
            ('end', 'End')],
        default='auto')
    selectorItemGap = fields.Integer(string='Selector Item Gap', default=7)
    selectorButtonGap = fields.Integer(string='Selector Button Gap', default=10)

    


