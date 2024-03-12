import os
import base64

from odoo import api, fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    logo = fields.Binary(default=lambda self: self._get_logo())

    def _get_logo(self):
        logo_filename = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static/img/logo_minsa.png")
        return base64.b64encode(open(logo_filename, "rb").read())

    @api.model_create_multi
    def create(self, vals_list):
        for values in vals_list:
            if not values.get("logo"):
                values.update({"logo": self._get_logo()})
        return super(ResCompany, self).create(vals_list)
