# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Modulo creado para la base de un modulo""",

    'description': """
        El proposito de este modulo es crear un modulo funcional
    """,

    'author': "OGGOnzanzalezM",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/openacademy_course_view.xml',
        'views/openacademy_session_view.xml',
        'views/partner_view.xml',
        'workflow/openacademy_session_workflow.xml',
    ],
    'installable':True,
    'auto_install':False,
}
