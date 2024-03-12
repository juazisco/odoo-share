# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsTitle(models.Model):
    '''
    Mana Dashboard Echarts Title
    '''
    _name = 'mana_dashboard.echarts_title'

    show = fields.Boolean(string='Show', default=True)
    text = fields.Char(string='Text', default='Mana Dashboard')
    link = fields.Char(string='Link', default='')
    target = fields.Char(string='Target', default='blank')
    textStyle = fields.Many2one(
        string='Text Style',
        comodel_name='mana_dashboard.text_style',
        ondelete='cascade')
    subtext = fields.Char(string='Subtext', default='')
    sublink = fields.Char(string='Sublink', default='')
    subtarget = fields.Char(string='Subtarget', default='blank')
    subtextStyle = fields.Many2one(
        string='Subtext Style',
        comodel_name='mana_dashboard.title_style',
        ondelete='cascade')
    textAlign = fields.Char(string='Text Align', default='auto')
    textVerticalAlign = fields.Char(string='Text Vertical Align', default='auto')
    padding = fields.Char(string='Padding', default='5')
    itemGap = fields.Integer(string='Item Gap', default=10)
    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=2)   
    left = fields.Char(string='Left', default='auto')
    top = fields.Char(string='Top', default='auto')
    right = fields.Char(string='Right', default='auto')
    bottom = fields.Char(string='Bottom', default='auto')
    backgroundColor = fields.Char(string='Background Color', default='transparent')
    borderColor = fields.Char(string='Border Color', default='#ccc')
    borderWidth = fields.Integer(string='Border Width', default=0)
    borderRadius = fields.Integer(string='Border Radius', default=0)
    shadowBlur = fields.Integer(string='Shadow Blur', default=0)
    shadowColor = fields.Char(string='Shadow Color', default='transparent')
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=0)
