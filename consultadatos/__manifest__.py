{
    "name": "Minsa -Consulta Datos",
    "author": "Daniel Mattos",
    "category": "Localisation/America",
    "summary": "Consulta de datos a Servicios",
    "description": """
        # Configuración
        Establecer los parametros de sistema mpi_api_host, mpi_api_token de MPI.

        # Servicios Disponibles
            - Consulta Reniec.
            - Consulta Mpi.

        # Dependencias python
            -mpi-client

    """,
    "website": "",
    "depends": [],
    "external_dependencies": {"python": ["mpi_client"]},
    "data": [
        "security/ir.model.access.csv",
        "data/consultadatos_data.xml",
        "views/views.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": False,
    "sequence": 1,
    "version": "17.0.0.0.0",
    "pre_init_hook": "pre_init_hook",
    "license": "LGPL-3",
}
