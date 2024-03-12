# Copyright <2011> <Daniel Reis, Maxime Chambreuil, Savoir-faire Linux>
# Copyright 2016 LasLabs Inc.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "External Database Source - MSSQL",
    "summary": "External Database Source for MSSQL Server using pyodbc and sqlalchemy",
    "version": "17.0.1.0.1",
    "category": "Tools",
    "author": "Daniel Reis, " "LasLabs, " "Odoo Community Association (OCA)",
    "maintainers": ["anddago78"],
    "website": "https://github.com/OCA/server-backend",
    "license": "LGPL-3",
    "depends": ["base_external_dbsource_sqlite"],
    "external_dependencies": {"python": ["pyodbc", "sqlalchemy"]},
    "demo": ["demo/base_external_dbsource.xml"],
    "installable": True,
}
