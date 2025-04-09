# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta


class DadesFactura(models.Model):
    _name = 'factures.factures'
    _description = 'Factures'

    state = fields.Selection(
        [
            ('draft', 'Esborrany')
            ('validated', 'Validada')
            ('sent', 'Enviada')
            ('paid', 'Pagada')
        ],
        string="Estat",
        default="draft"
    )

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

    # Metodes per canviar l'estat de la factura
    def action_validate(self):
        for record in self:
            record.state = 'validated'

    def action_sent(self):
        for record in self:
            record.state = 'sent'

    def action_paid(self):
        for record in self:
            record.state = 'paid'


    """
    Falta comprovar les seguents funcions:
    """
    # Metode que avisa en cas de que una factura no s'hagi pagat
    def comprova_factures_impagades(self):
        # Buscar factures no pagades amb mes de 30 dies de termini de venciment
        factures = self.search([
            ('state', '!=', 'paid'),
            ('data_creacio_factura', '<=', fields.Date.context_today(self) - timedelta(days=30))
        ])

        # Enviar notificacions
        for factura in factures:
            self.env['mail.message'].create({
                'model': 'factures.factures',
                'res_id': factura.id,
                'message_type': 'notification',
                'subtype_id': self.env.ref('mail.mt_note').id,
                'body': f"La factura {factura.name} no ha estat pagada dins del termini",
                'author_id': self.env.user.partner_id.id,
                'partner_ids': [(4, self.env.ref('base.user_admin').partner_id.id)]
            })

    # Metode per crear el cron que crea la funcio comprova_factures_impagades
    @api.model
    def create_cron_comprova_impagades(self):
        cron = self.env['ir.cron'].create({
            'name': 'Comprovacio factures impagades',
            'model_id': self.env.ref('factures.factures').id,
            'state': 'code',
            'user_id': self.env.user.id,
            'code': 'model.comprova_factures_impagades()',
            'interval_number': 1,
            'interval_type': 'days',
            'nextcall': fields.Datetime.now()
        })

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
