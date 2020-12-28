# -*- coding: utf-8 -*-
{
    'name': "mon_parc",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Mon parc",
    'website': "http://ilammedia.ma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Human Resources/Fleet',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'fleet', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/chauffeur.xml',
        'views/tracteur.xml',
        'views/remorque.xml',
        'views/trajets.xml',
        'views/voyage.xml',
        'views/clients.xml',
        # 'views/templates.xml',
    ],
    'images': [
        'static/description/icon.png',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}
