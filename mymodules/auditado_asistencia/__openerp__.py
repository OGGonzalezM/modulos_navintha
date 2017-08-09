# -*- coding: utf-8 -*-
{
    'name': "Indexol-auditados",

    'summary': """
        Modulo de Auditorias""",

    'description': """
        Para agregar campo de confirmacion de asistencia en auditados
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','res.users'],

    # always loaded Recurde cargar deacuerdo al orden deseado
    'data': [
        'views/confirmarasistencia_view.xml',
    ],
    'installable':True,
    'auto_install':False,
}
