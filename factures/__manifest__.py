# -*- coding: utf-8 -*-
{
    'name': "factures",

    # Dependencies del modul
    'depends': ['base', 'gestio_clients'],

    # Arxius carregats sempre
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

    # Arxiu a carregar en mode demostracio
    'data': [
        'demo/demo.xml',
    ],
}

