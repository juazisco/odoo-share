# -*- coding: utf-8 -*-
import pytz

from datetime import datetime, timedelta

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        index=True,
        default=lambda self: self.env.user.company_id,
    )
    user_id = fields.Many2one('res.users', 'Propietario', default=lambda self: self.env.user)
    check_in_photo = fields.Binary("Foto de ingreso", tracking=True)
    check_in_latitude = fields.Float("Latitud ingreso", tracking=True)
    check_in_longitude = fields.Float("Longitud ingreso", tracking=True)
    check_out_photo = fields.Binary("Foto de salida", tracking=True)
    check_out_latitude = fields.Float("Latitud salida", tracking=True)
    check_out_longitude = fields.Float("Longitud salida", tracking=True)

    def write(self, vals):
        attendances_dates = self._get_attendances_dates()
        if 'check_out' in vals:
            dt_string = vals['check_out']
            if dt_string is str:
                dt_format = '%Y-%m-%dT%H:%M:%S.%f'
                dt_object = datetime.strptime(dt_string, dt_format)
                dt_string = dt_object.strftime('%Y-%m-%d %H:%M:%S')
                vals['check_out'] = dt_string
        super(HrAttendance, self).write(vals)
        if any(field in vals for field in ['employee_id', 'check_in', 'check_out']):
            # Merge attendance dates before and after write to recompute the
            # overtime if the attendances have been moved to another day
            for emp, dates in self._get_attendances_dates().items():
                attendances_dates[emp] |= dates
            self._update_overtime(attendances_dates)

    @api.model
    def create(self, vals):
        remote_ids = self.env.user.employee_id.remote_ids
        lima = pytz.timezone('America/Lima')
        now = datetime.now(lima)
        now_naive = now.replace(tzinfo=None)
        adjusted_datetime = now_naive + timedelta(hours=5)
        vals.update({'check_in': adjusted_datetime})
        for record in remote_ids:
            if record.is_between_dates(record.start_date, record.end_date):
                return super(HrAttendance, self).create(vals)

        # If the condition is not met or remote_ids is empty, cancel the creation
        raise ValidationError('Ud. no tiene permitido registrar su asistencia por este medio.')


class HrAttendanceRemote(models.Model):
    _name = 'hr.attendance.remote'
    _description = 'Remote attendance'

    employee_id = fields.Many2one('hr.employee', u'Empleado')
    start_date = fields.Date("Fecha de inicio", required=True)
    end_date = fields.Date("Fecha de término", required=True)

    @staticmethod
    def is_between_dates(start_date, end_date):
        current_date = datetime.now().date()
        return start_date <= current_date <= end_date

    @api.onchange('start_date')
    def onchange_start_date(self):
        if not self.start_date:
            return
        current_date = datetime.now().date()
        if self.start_date < current_date:
            return {
                'value': {
                    'start_date': False,
                },
                'warning': {
                    'title': 'Error en fecha de inicio',
                    'message': 'La fecha de inicio no puede ser anterior al día de hoy.',
                },
            }

    @api.onchange('end_date')
    def onchange_end_date(self):
        if not self.end_date:
            return
        if self.end_date < self.start_date:
            return {
                'value': {
                    'end_date': False,
                },
                'warning': {
                    'title': 'Error en fecha de término',
                    'message': 'La fecha de término no puede ser anterior a la fecha de inicio.',
                },
            }
