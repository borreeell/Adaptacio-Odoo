# -*- coding: utf-8 -*-
{
    'name': "Registre de clients",

    # Moduls dels que depen aquest modul
    'depends': ['base'],

    # Arxius que estan carregats sempre
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/ir_sequence.xml'
    ],
    # Arxius que només es carreguen en mode de demostració
    'demo': [
        'demo/demo.xml',
    ],
    
    'application': True,
    'installable': True,
    'auto_install': False,
}

