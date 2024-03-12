
# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ManaDashboardAssetsSubType(models.Model):
    '''
    Model Project
    '''
    _name = 'mana_dashboard.assets_sub_type'
    _description = 'Mana Dashboard Assets Sub Type'

    name = fields.Char(string='name', required=True)

    # name must be unique
    _sql_constraints = [('name_unique', 'unique(name)', 'name must be unique')]
