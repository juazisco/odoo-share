# -*- coding: utf-8 -*-
import base64
import csv

from odoo import api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import UserError

FIRST_TYPE = '01'
SELECTION_REPORT_TYPES = [(FIRST_TYPE,
                           'REPORTE DE REGISTRO DE ASISTENCIAS')]

REPORT_NAME = 'oehealth_samu.guardchief_report_template1'

EXPORT_FILE_NAME = '/mnt/extra-addons/attendances.dat'


class HrAttendanceReportWizard(models.TransientModel):
    _name = 'hr.attendance.report.wizard'

    start_date = fields.Date('Fecha (desde)', required=True)
    end_date = fields.Date('Fecha (hasta)', required=True)
    report_type = fields.Selection(SELECTION_REPORT_TYPES,
                                   'Tipo de reporte',
                                   default=FIRST_TYPE,
                                   required=True)
    csv_data = fields.Binary()
    filename = fields.Char()

    @api.model
    def default_get(self, fields_list):
        res = super(HrAttendanceReportWizard, self).default_get(fields_list)
        today = fields.Date.from_string(fields.Date.context_today(self))
        res.update({
            'start_date': str(today.replace(day=1)),
            'end_date': str(today)
        })
        return res

    @property
    def _get_content(self):
        return self._build_report()

    @staticmethod
    def _get_current_datetime(ddatetime=False):
        datetime_format = '%Y-%m-%d %H:%M:%S'
        start_datetime = datetime.strptime(
            ddatetime, datetime_format) if ddatetime else datetime.now()
        datetime_format = '%d-%m-%Y %H:%M:%S'
        return (start_datetime - timedelta(hours=5)).strftime(datetime_format)

    @staticmethod
    def _get_current_datetime_data(ddatetime=False):
        datetime_format = '%Y-%m-%d %H:%M:%S'
        start_datetime = datetime.strptime(
            ddatetime, datetime_format) if ddatetime else datetime.now()
        # datetime_format = '%Y-%m-%d %H:%M:%S'
        return (start_datetime - timedelta(hours=5)).strftime(datetime_format)

    @staticmethod
    def _get_ddmmyy_format_date(ddate=False):
        date_format = '%Y-%m-%d'
        ddate = datetime.strptime(ddate,
                                  date_format) if ddate else datetime.now()
        datetime_format = '%d-%m-%Y'
        return ddate.strftime(datetime_format)

    def _real_datetime(self, ddatetime):
        return self._get_current_datetime(ddatetime) if ddatetime else ''

    def download_pdf(self):
        if isinstance(self.start_date, str):
            self.start_date = datetime.strptime(self.start_date, '%Y-%m-%d').date()

        if isinstance(self.end_date, str):
            self.end_date = datetime.strptime(self.end_date, '%Y-%m-%d').date()

        if self.start_date > self.end_date:
            raise UserError(
                'La fecha de inicio no puede ser posterior a la fecha final.')

        utc_5 = datetime.strptime(datetime.strftime(
            datetime.now() - timedelta(hours=5), '%Y-%m-%d'), '%Y-%m-%d').date()

        if self.end_date > utc_5:
            raise UserError(
                f'La fecha final no puede ser posterior al día de hoy ({utc_5}).')

        # csv header
        fieldnames = ['dni', 'fecha', 'x', 'x1', 'x2', 'x3']

        rows = self._build_report()
        with open(EXPORT_FILE_NAME, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter='\t')
            # writer.writeheader()
            if len(rows) == 0:
                rows.append({"dni": "No existen registros"})
            writer.writerows(rows)

        with open(EXPORT_FILE_NAME, 'r') as f2:
            # file encode and store in a variable ‘data’
            data = str.encode(f2.read(), 'utf-8')
            self.csv_data = base64.encodebytes(data)

        self.filename = EXPORT_FILE_NAME
        return {
            'type': 'ir.actions.act_url',
            'url': "web/content/?model=hr.attendance.report.wizard&id=" + str(self.id)
                    + "&filename=asistencias.dat&field=csv_data&download=true&filename=" + self.filename,
            'target': 'new',
        }

    def _build_report(self, domain=[], ttype=[]):
        data = []

        select = """
        SELECT
        employee.identification_id as dni,
        attendance.check_in as fecha,
        1 as f1,
        0 as f2,
        0 as f3,
        0 as f4
        FROM hr_attendance attendance
        inner join hr_employee employee on employee.id = attendance.employee_id
        WHERE attendance.check_in::TIMESTAMP BETWEEN ('{start} 00:00:00'::TIMESTAMP + INTERVAL '5 hours') AND ('{end} 23:59:59'::TIMESTAMP + INTERVAL '5 hours')
        AND attendance.company_id = '{cia}'
        union
        SELECT
        employee.identification_id as dni,
        attendance.check_out as fecha,
        1 as f1,
        0 as f2,
        0 as f3,
        0 as f4
        FROM hr_attendance attendance
        inner join hr_employee employee on employee.id = attendance.employee_id
        WHERE attendance.check_out::TIMESTAMP BETWEEN ('{start} 00:00:00'::TIMESTAMP + INTERVAL '5 hours') AND ('{end} 23:59:59'::TIMESTAMP + INTERVAL '5 hours')
        AND attendance.company_id = '{cia}'
        """.format(start=self.start_date, end=self.end_date, cia=self.env.user.company_id.id)

        records = self.env.cr.execute(select)
        records = self.env.cr.fetchall()
        if records:
            for record in records:
                vals = {
                    'dni': record[0],
                    'fecha': self._get_current_datetime_data(str(record[1]).split('.')[0]),
                    'x': record[2],
                    'x1': record[3],
                    'x2': record[4],
                    'x3': record[5],
                }
                data.append(vals)
        return data
