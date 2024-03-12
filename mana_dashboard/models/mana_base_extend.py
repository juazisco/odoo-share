# -*- coding: utf-8 -*-

from odoo import models, api, exceptions, fields, _, tools
from odoo.exceptions import ValidationError
from odoo.fields import Field
from odoo.osv import expression
from odoo.tools import Query
import logging

_logger = logging.getLogger(__name__)


class ManaBaseExtend(models.AbstractModel):
    """
    base extend
    """
    _inherit = "base"

    @api.model
    def _add_inherited_fields(self):
        """
        extend to add custom code
        """
        super(ManaBaseExtend, self)._add_inherited_fields()
        self._after_inherited_fields()

    @api.model
    def _add_field_ext(self, name, field):
        """ Add the given ``field`` under the given ``name`` in the class """
        self._add_field(name, field)

    @api.model
    def name_search_ext(self, name='', args=None, operator='ilike', limit=10, extra_fields=None):
        """ 
        Search for records that have a display name matching the given ``name``. 
        """
        ids = self._name_search(name, args, operator, limit=limit, order=self._order)

        if isinstance(ids, Query):
            records = self._fetch_query(ids, self._determine_fields_to_fetch(['display_name']))
        else:
            # Some override of `_name_search` return list of ids.
            records = self.browse(ids)
            records.fetch(['display_name'])
            
        record_cache = {record.id: record for record in records}
        results = [(record.id, record.display_name) for record in records.sudo()]
        last_results = []
        for result in results:
            record = record_cache[result[0]]
            if extra_fields:
                for field in extra_fields:
                    result += (record[field],)
            last_results.append(result)
        return last_results
