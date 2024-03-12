
# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions, _
import json
import json5


class ManaDashboardSearchInfo(models.Model):
    '''
    Search Info
    '''
    _name = 'mana_dashboard.search_info'
    _description = 'Mana Dashboard Search Info'

    name = fields.Char(string='name', required=True)
    dashboard_id = fields.Many2one(
        string='dashboard_id', comodel_name='mana_dashboard.dashboard')
    uid = fields.Many2one(string='uid', comodel_name='res.users')
    search_infos = fields.Text(string='search infos')
    
    # dashboard and name must be unique
    _sql_constraints = [
        ('dashboard_id_name_unique', 'unique(dashboard_id, name)', _('Dashboard and name must be unique!'))
    ]
        
    def reset_search_infos(self, dashboard_id):
        """
        reset search info
        """
        records = self.env['mana_dashboard.search_info'].search([
            ('dashboard_id', '=', dashboard_id),
            ('uid', '=', self.env.uid)
        ])
        records.unlink()
        self.clear_caches()

    def update_search_infos(self, dashboard_id, search_infos):
        """
        update serach info
        """
        # get the old search info
        old_infos = self.search([
            ('dashboard_id', '=', dashboard_id),
            ('uid', '=', self.env.uid)
        ]) 
        old_infos_dict = {}
        for old_info in old_infos:
            old_infos_dict[old_info.name] = old_info

        # get delete infos
        delete_infos = []
        for old_info_name in old_infos_dict:
            if old_info_name not in search_infos:
                delete_infos.append(old_info_name)

        for delete_info in delete_infos:
            old_infos_dict[delete_info].unlink()

        # get update infos
        update_infos = []
        for old_info_name in old_infos_dict:
            if old_info_name in search_infos:
                update_infos.append(old_info_name)
                
        for update_info in update_infos:
            old_infos_dict[update_info].search_infos = json.dumps(search_infos[update_info])

        # get create infos
        create_infos = []
        for search_info in search_infos:
            if search_info in old_infos_dict:
                continue
            create_infos.append(search_info)
            
        for name in create_infos:
            self.env['mana_dashboard.search_info'].create({
                'name': name,
                'dashboard_id': dashboard_id,
                'uid': self.env.uid,
                'search_infos': json.dumps(search_infos[name])
            })
    
    def get_search_info(self, dashboard_id, name):
        """
        get search info
        """
        records = self.env['mana_dashboard.search_info'].search([
            ('dashboard_id', '=', dashboard_id),
            ('uid', '=', self.env.uid),
            ('name', '=', name)
        ], limit=1)
        if not records:
            return {}
        
        result = {}
        for record in records:
            result[record.name] = json.loads(record.search_infos)
        
        return result

    def get_search_infos(self, dashboard_id):
        """
        get search infos
        """
        records = self.env['mana_dashboard.search_info'].search([
            ('dashboard_id', '=', dashboard_id),
            ('uid', '=', self.env.uid)
        ])
        if not records:
            return {}
        
        result = {}
        for record in records:
            result[record.name] = json5.loads(record.search_infos)
        
        return result