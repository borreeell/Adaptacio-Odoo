# -*- coding: utf-8 -*-
{
    'name': "factures",

    # any module necessary for this one to work correctly
    'depends': ['base', 'gestio_clients'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/ir_sequence.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': True,
}

