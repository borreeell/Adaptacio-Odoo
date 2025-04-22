# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta


class DadesFactura(models.Model):
    _name = 'factures.factures'
    _description = 'Factures'

    name = fields.Char(
        string="Nº de factura:",
        required=False,
        copy=False,
        readonly=True
    )

    id_client = fields.Many2one(
        'gestio_clients.gestio_clients',
        string="ID del client"
    )

    data_creacio_factura = fields.Date(
        string="Data factura:",
        default=fields.Date.context_today
    )

    termini_pagament = fields.Integer(
        string="Termini pagament",
        default=30
    )

    articles_factura = fields.One2many(
        'factures.articles_factura',
        'factura_id',
    )

    # Metode per crear la sequencia per l'identificador del programa
    @api.model
    def create(self, vals):
        if 'name' not in vals or not vals['name']:
            vals['name'] = self.env['ir.sequence'].next_by_code('factures.sequence')
        return super(DadesFactura, self).create(vals)

    # Metode per calcular la data de venciment de la factura
    @api.depends('data_creacio_factura', 'termini_pagament')
    def _compute_data_venciment(self):
        for record in self:
            if record.data_creacio_factura:
                record.data_venciment = record.data_creacio_factura + timedelta(days = record.termini_pagament)

class ArticlesFactura(models.Model):
    _name = "factures.articles_factura"
    _description = "Articles de la factura"

    factura_id = fields.Many2one(
        'factures.factures'
    )

    id_article = fields.Char(
        string="ID de l'article"
    )

    nom_article = fields.Char(
        string="Nom de l'article"
    )

    quantitat = fields.Integer(
        string="Quantitat"
    )

    preu_unitari = fields.Float(
        string="Preu unitari"
    )

    preu_subtotal = fields.Float(
        string="Preu subtotal",
        compute='_compute_preu_subtotal'
    )

    percentatge_iva = fields.Float(
        string="Percentatge IVA"
    )

    preu_total = fields.Float(
        string="Preu total",
        compute='_compute_preu_total'
    )

    @api.depends('quantitat', 'preu_unitari', 'percentatge_iva')
    def _compute_preu_subtotal(self):
        for record in self:
            record.preu_subtotal = record.quantitat * record.preu_unitari
    
    @api.depends('preu_subtotal', 'percentatge_iva')
    def _compute_preu_total(self):
        for record in self:
            record.preu_total = record.preu_subtotal * (1 + record.percentatge_iva / 100)