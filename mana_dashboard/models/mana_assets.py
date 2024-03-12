
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.mimetypes import guess_mimetype

class ManaDashboardAssets(models.Model):
    '''
    Mana Dashboard Assets
    '''
    _name = 'mana_dashboard.assets'
    _description = 'assets'
    _order = 'sequence asc'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer(string='sequence', default=10)
    file = fields.Binary(string='File', required=True)
    type = fields.Many2one(
        string="Main Type", 
        comodel_name='mana_dashboard.assets_type')
    system = fields.Boolean(string='system', default=False)
    sub_type = fields.Many2one(
        string='Type', 
        comodel_name='mana_dashboard.assets_sub_type')
    url = fields.Char(string='url', compute='_compute_url')

    @api.depends('file')
    def _compute_url(self):
        for record in self:
            record.url = '/web/content/mana_dashboard.assets/%s/file/%s' % (record.id, record.name)

    def get_asset_data(self):
        """
        get assets data
        """
        self.ensure_one()
        data = self.file
        mine_type = guess_mimetype(data)
        # convert to base64 image url
        if mine_type:
            data = "data:%s;base64,%s" % (mine_type, data.decode('utf-8'))
            return {
                'src': data
            }
        else:
            return self.url
