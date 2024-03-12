# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ManaDashboardConfig(models.Model):
    '''
    Dashboard Config
    '''
    _name = 'mana_dashboard.config'
    _inherit = [
        'mana_dashboard.config_base', 
        'mana_dashboard.template_base',
        'mana_dashboard.data_source',
        'mana_dashboard.theme_base'
    ]
    _description = 'Mana Dashboard Config'
    _rec_name = 'config_name'

    # as related and compute from mixin not work, so we override it here
    template_id = fields.Many2one(
        string='Template',
        comodel_name='mana_dashboard.template')

    supported_data_source_types = fields.Many2many(
        comodel_name='mana_dashboard.data_source_type',
        related='template_id.supported_data_source_types')

    data_source_type_domain_ids = fields.One2many(
        string='Data Source Type Domain',
        compute='_compute_data_source_type_domain_ids',
        comodel_name='mana_dashboard.data_source_type')

    supported_result_types = fields.Many2many(
        string='Supported Result Types',
        comodel_name='mana_dashboard.result_type',
        related='template_id.supported_result_types')

    result_type_domain_ids = fields.One2many(
        string='Result Type Domain',
        comodel_name='mana_dashboard.result_type',
        compute='_compute_result_type_domain_ids')
    
    @api.model
    def get_next_name(self):
        """
        get next name
        """
        name = self.env['ir.sequence'].next_by_code('dashboard.config.sequence')
        while self.search([('config_name', '=', name)]):
            name = self.env['ir.sequence'].next_by_code('dashboard.config.sequence')
        return name

    @api.model
    def create_config(self, dashboard_id, options = {}):
        """
        create custom config
        """
        if options.get('default_template'):
            template = self.env.ref(options.get('default_template'), raise_if_not_found=False)
        else:
            template = False

        if options.get('template'):
            dashboard = self.env['mana_dashboard.dashboard'].browse(dashboard_id)
            template = options.get('template')
            template = self.env['mana_dashboard.template'].search([
                ('name', '=', template),
                ('is_custom', '=', True),
                ('dashboard_template_id', '=', dashboard.template_id.id),
            ])

        if options.get('template_category'):
            template_category = options.get('template_category')
        else:
            template_category = False

        # template type
        if options.get('template_type'):
            template_type = options.get('template_type')
        else:
            template_type = False

        name = self.get_next_name()

        config = {
            'dashboard_id': dashboard_id,
            'template_id': template.id if template else False,
            'config_name': name,
            
            'scripts': template.scripts if template else False,
            'default_scripts': template.default_scripts if template else False,
            'styles': template.styles if template else False,
            'template': template.template if template else False,
        
            'demo_template': template.demo_template if template else False,
            'demo_data': template.demo_data if template else False, 
            
            'template_category': template_category,
            'template_type': template_type,
        }

        if template and not template.multi_data_source:
            # data source type
            config['data_source_type'] = \
                template.default_data_source_type.id if not template.multi_data_source else False
            # code
            config['code'] = template.default_code if template else False
            # sql
            config['sql'] = template.default_sql if template else False
            # json
            config['json_data'] = template.default_json if template else False
            # result type
            config['result_type'] = template.default_result_type.id if template else False
            
        record = self.create(config)
        return record

    @api.depends('template_category', 'template_type')
    def _compute_template_domain_ids(self):
        """
        if has a drill up category, it is a drill down config
        """
        for record in self:
            if record.template_category and not record.drill_up_config:
                domain = [('category', '=', record.template_category)]
                if record.template_type:
                    domain.append(('type', '=', record.template_type))
                record.template_domain_ids = self.env['mana_dashboard.template'].search(domain).ids or False
            else:
                record.template_domain_ids = self.env['mana_dashboard.template'].search([]).ids or False

    @api.depends('supported_data_source_types')
    def _compute_data_source_type_domain_ids(self):
        """
        override this method to set the domain of data source type
        """
        for record in self:
            if record.supported_data_source_types:
                record.data_source_type_domain_ids = record.supported_data_source_types.ids
            else:
                record.data_source_type_domain_ids = self._get_data_source_types()

    @api.depends('supported_result_types')
    def _compute_result_type_domain_ids(self):
        for record in self:
            record.result_type_domain_ids = self._get_result_types()

    def export_config(self):
        """
        export config
        """
        self.ensure_one()
        
        config = {
            'id': self.id,
            'dashboard_id': self.dashboard_id.id,
            'config_name': self.config_name,
            'template_name': self.template_id.name,
            'template_category': self.template_category,
            'template_type': self.template_type,
            'scripts': self.scripts, 
            'template': self.template,
            'styles': self.styles,
            'scripts': self.scripts,
            'code': self.code,
            'json_data': self.json_data,
            'sql': self.sql,
            'default_scripts': self.default_scripts,
            'disable_children': self.disable_children,
            'disable_first_child': self.disable_first_child,
            'demo_template': self.demo_template,
            'demo_data': self.demo_data,
            'preview_background_color': self.preview_background_color,
            'theme_info': self.theme_info,
            'data_source_mode': self.data_source_mode,
            'domain': self.domain,
            'context': self.context,
            'limit': self.limit,
        }

        if not self.multi_data_source:
            config['multi_data_source'] = False
            data_source_info = self.data_source_mixin_id.export_data_source_mixin()
            config['data_source_info'] = data_source_info
        else:   
            config['multi_data_source'] = True
            config['data_source_infos'] = []
            for data_source_id in self.data_source_ids:
                data_source_info = data_source_id.export_data_source()
                config['data_source_infos'].append(data_source_info)

        return config

    @api.model
    def import_config(self, config_info):
        """
        import config
        """
        config = {}
        if not config_info.get('multi_data_source'):
            config['multi_data_source'] = False
            data_source_mixin = self.env['mana_dashboard.data_source_mixin'].import_data_source_mixin(
                config_info['data_source_info'])
            config['data_source_mixin_id'] = data_source_mixin.id
        else:
            config['multi_data_source'] = True
            data_source_ids = []
            for data_source_info in config_info['data_source_infos']:
                data_source = self.env['mana_dashboard.data_source'].import_data_source(data_source_info)
                data_source_ids.append(data_source.id)
            config['data_source_ids'] = data_source_ids
        
        # ensure the config name
        config['config_name'] = config_info.get('config_name')
        if not config['config_name']:
            config['config_name'] = self.get_next_name()

        config['template_category'] = config_info.get('template_category')
        config['template_type'] = config_info.get('template_type')
        if config_info.get('template_name'):
            domain = [('name', '=', config_info['template_name'])]
            if config_info.get('template_category'):
                domain.append(('category', '=', config_info['template_category']))
            if config_info.get('template_type'):
                domain.append(('type', '=', config_info['template_type']))
            config['template_id'] = self.env['mana_dashboard.template'].search(domain, limit=1).id

        config['scripts'] = config_info.get('scripts')
        config['template'] = config_info.get('template')
        config['demo_template'] = config_info.get('demo_template')

        config['json_data'] = config_info.get('json_data')
        config['sql'] = config_info.get('sql')
        config['code'] = config_info.get('code')

        config['styles'] = config_info.get('styles')
        config['default_scripts'] = config_info.get('default_scripts')
        config['demo_data'] = config_info.get('demo_data')
        config['preview_background_color'] = config_info.get('preview_background_color')
        config['domain'] = config_info.get('domain')
        config['context'] = config_info.get('context')
        config['limit'] = config_info.get('limit')

        # theme info
        config['theme_info'] = config_info.get('theme_info')

        return self.create(config)
    
    def save_theme_info(self, theme_info):
        """
        save theme info
        """
        self.ensure_one()
        self.theme_info = theme_info
        return True
