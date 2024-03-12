from odoo import models, api

TZ = "America/Lima"


class Resuser(models.Model):
    _inherit = "res.users"

    @api.model_create_multi
    def create(self, vals_list):
        for values in vals_list:
            if not values.get("tz", False):
                values.update(dict(tz=TZ))
        return super(Resuser, self).create(vals_list)
