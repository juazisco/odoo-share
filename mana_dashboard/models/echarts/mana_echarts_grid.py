# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsGrid(models.Model):
    '''
    Mana Dashboard Text Style
    '''
    _name = 'mana_dashboard.echarts_grid'

    show = fields.Boolean(string='Show', default=True)
    zlevel = fields.Integer(string='Zlevel', default=0)
    z = fields.Integer(string='Z', default=2)
    left = fields.Char(string='Left', default='10%')
    top = fields.Char(string='Top', default='60')
    right = fields.Char(string='Right', default='10%')
    bottom = fields.Char(string='Bottom', default='60')
    width = fields.Char(string='Width', default='auto')
    height = fields.Char(string='Height', default='auto')
    containLabel = fields.Boolean(string='Contain Label', default=False)
    backgroundColor = fields.Char(string='Background Color', default='transparent')
    borderColor = fields.Char(string='Border Color', default='#ccc')
    borderWidth = fields.Integer(string='Border Width', default=0)
    shadowBlur = fields.Integer(string='Shadow Blur', default=0)
    shadowColor = fields.Char(string='Shadow Color', default='transparent')
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=0)
