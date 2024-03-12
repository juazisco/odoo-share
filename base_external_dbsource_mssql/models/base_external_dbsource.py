# Copyright 2011 Daniel Reis
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import pyodbc

from odoo import fields, models

assert pyodbc


class BaseExternalDbsource(models.Model):
    """It provides logic for connection to a MSSQL data source."""

    _inherit = "base.external.dbsource"

    connector = fields.Selection(
        selection_add=[("mssql", "Microsoft SQL Server")], ondelete={"mssql": "cascade"}
    )
    PWD_STRING_MSSQL = "Password=%s;"

    def connection_close_mssql(self, connection):
        return connection.close()

    def connection_open_mssql(self):
        return self._connection_open_sqlalchemy()

    def execute_mssql(self, sqlquery, sqlparams, metadata):
        return self._execute_sqlalchemy(sqlquery, sqlparams, metadata)

    def execute_mssql_dict(self, sqlquery, sqlparams):
        rows, cols = self._execute_sqlalchemy(sqlquery, sqlparams, True)
        list_dict = []        
        for row in rows:
            r_dict = {}
            cnt = 0
            for item in row:
                r_dict[cols[cnt]] = item
                cnt += 1
            list_dict.append(r_dict)
        return list_dict

