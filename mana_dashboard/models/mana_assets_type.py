
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ManaDashboardAssetsType(models.Model):
    '''
    Assets Type
    '''
    _name = 'mana_dashboard.assets_type'
    _description = 'assets type'

    name = fields.Char(string='name', required=True)
