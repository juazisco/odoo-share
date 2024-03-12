# -*- coding: utf-8 -*-
{
    'name': "Minsa: Theme",

    'summary': "Módulo Theme Minsa",

    'description': """
Configuración del theme para Minsa
    """,

    'author': "Minsa",
    'website': "https://www.minsa.gob.pe",
    'category': 'Themes/Backend',
    'version': '17.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['l10n_minsa','muk_web_theme'],

    # always loaded
    'data': [     
        'data/base.xml',
        'views/ir_ui_menu.xml',
        'views/web_login_template.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "minsa_theme/static/src/scss/indicator_button.scss",
            "minsa_theme/static/src/xml/template.xml",
        ],
    },
    'installable': True,
    'license': 'LGPL-3',
}

