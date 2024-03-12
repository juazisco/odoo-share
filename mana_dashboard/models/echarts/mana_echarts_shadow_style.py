# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsShadowStyle(models.Model):
    '''
    Mana Dashboard Shadow Style
    '''
    _name = 'mana_dashboard.echarts_shadow_style'

    color = fields.Char(string='Color', default='transparent')
    shadowBlur = fields.Integer(string='Shadow Blur', default=0)
    shadowColor = fields.Char(string='Shadow Color', default='transparent')
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=0)
    opacity = fields.Float(string='Opacity', default=1)
