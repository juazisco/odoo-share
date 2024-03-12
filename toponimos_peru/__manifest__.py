{
    "name": "Toponimos de Peru",
    "summary": """
        Ubigeo Departamentos, Provincias y distritos del Peru según INEI.
    """,
    "description": """
        Localizacion Peruana.
            * Tabla de Ubigeos - Según INEI 2016
            * Departamentos, provincias y distritos de todo el Perú
    """,
    "author": "",
    "website": "",
    "category": "Uncategorized",
    "version": "17.0.0.0.0",
    "depends": ["base"],
    "data": [
        "views/res_partner_view.xml",
        "views/res_country_view.xml",
        "data/res_country_data.xml",
        "data/res.country.state.csv",
        "data/patch1/res.country.state.csv",
        "data/patch2/res.country.state.csv",
    ],
    "demo": [],
    "license": "LGPL-3",
}
