# -*- coding: utf-8 -*-

from odoo import fields, models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    remote_ids = fields.One2many(comodel_name='hr.attendance.remote', inverse_name='employee_id', string='Visitantes', track_visibility='onchange')
