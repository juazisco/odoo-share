# -*- coding: utf-8 -*-

import inspect

from odoo import models, _
from odoo.exceptions import AccessError
from odoo.models import check_method_name


class ManaViewExtend(models.Model):
    '''
    extend to add save and notify and just notify
    '''
    _inherit = 'ir.ui.view'

    def _validate_tag_button(self, node, name_manager, node_info):

        if not node_info['validate']:
            return
        
        special = node.get('special')
        if special and special in ['save_and_notify', 'just_notify']:
            return
        
        super(ManaViewExtend, self)._validate_tag_button(
            node, name_manager, node_info)
