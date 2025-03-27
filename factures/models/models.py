# -*- coding: utf-8 -*-

from odoo import models, fields, api


class factures(models.Model):
    _name = 'factures.factures'
    _description = 'factures.factures'

    name = fields.Char(
        string="Nº d'albara:"
    )
