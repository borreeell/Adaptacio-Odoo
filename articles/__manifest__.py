# -*- coding: utf-8 -*-
{
    'name': "Articles",

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/ir_sequence.xml'
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'application': True,
    'installable': True,
    'auto_install': False,
}
