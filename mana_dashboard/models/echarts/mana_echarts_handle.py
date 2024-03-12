# -*- coding: utf-8 -*-

from odoo import models, fields, _


class EchartsHandle(models.Model):
    '''
    Mana Dashboard Echarts Handle
    '''
    _name = 'mana_dashboard.echarts_handle'

    show = fields.Boolean(string='Show', default=True)
    icon = fields.Char(
        string='Icon', 
        default='image://data:image/gif;base64,R0lGODlhEAAQAMQAAORHHOVSKudfOulrSOp3WOyDZu6QdvCchPGolfO0o/XBs/fNwfjZ0frl3/zy7////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAkAABAALAAAAAAQABAAAAVVICSOZGlCQAosJ6mu7fiyZeKqNKToQGDsM8hBADgUXoGAiqhSvp5QAnQKGIgUhwFUYLCVDFCrKUE1lBavAViFIDlTImbKC5Gm2hB0SlBCBMQiB0UjIQA7')
    size = fields.Integer(string='Size', default=15)
    margin = fields.Char(string='Margin', default='5%')
    color = fields.Char(string='Color', default='#333')
    throttle = fields.Integer(string='Throttle', default=100)
    shadowBlur = fields.Integer(string='Shadow Blur', default=3)
    shadowColor = fields.Char(string='Shadow Color', default='#aaa')
    shadowOffsetX = fields.Integer(string='Shadow Offset X', default=0)
    shadowOffsetY = fields.Integer(string='Shadow Offset Y', default=2)
