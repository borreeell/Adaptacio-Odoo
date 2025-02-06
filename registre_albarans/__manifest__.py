# -*- coding: utf-8 -*-
{
    'name': "registre_albarans",
    'summary': "Registre i gestio d'albarans",
    'author': "Pau Borrell",
    'version': '0.1',

    # Moduls del que depen aquest modul
    'depends': ['base', 'gestio_clients'],

    # Arxius que es carreguen
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/ir_sequence.xml',
    ],
    # Nomes es carrega en mode demo (no s'hi dona cap us)
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

