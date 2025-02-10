from odoo import models, fields, api


class Albara(models.Model):
    _name = 'registre_albarans.registre_albarans'
    _description = 'Albarans'

    name = fields.Char(
        string="Nº d'albara:",
        required=True,
        copy=False,
        readonly=True,
    )
    id_client = fields.Many2one(
        'gestio_clients.gestio_clients',
        string="ID del client",
    )
    id_reparation = fields.Char(
        string="ID de la reparacio",
    )
    date = fields.Date(
        string="Data albara",
        default=fields.Date.context_today,
        required=True
    )
    articles_albara = fields.One2many('registre_albarans.articles_albara', 'albara_id', string="Articles")

    @api.model
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('registre_albarans.sequence') or '/'
        return super(Albara, self).create(vals_list)
    
class ArticlesAlbara(models.Model):
    _name = 'registre_albarans.articles_albara'
    _description = 'Articles de l\'albara'

    albara_id = fields.Many2one('registre_albarans.registre_albarans')
    id_article = fields.Char(string="ID de l'article")
    nom_article = fields.Char(string="Nom de l'article")
    quantitat = fields.Integer(string="Quantitat")
    preu_unitari = fields.Float(string="Preu unitari")
    preu_subtotal = fields.Float(string="Preu subtotal", compute='_compute_preu_subtotal')
    percentatge_iva = fields.Float(string="Percentatge IVA")
    preu_total = fields.Float(string="Preu total", compute='_compute_preu_total')

    @api.depends('quantitat', 'preu_unitari', 'percentatge_iva')
    def _compute_preu_subtotal(self):
        for record in self:
            record.preu_subtotal = record.quantitat * record.preu_unitari
    
    @api.depends('preu_subtotal', 'percentatge_iva')
    def _compute_preu_total(self):
        for record in self:
            record.preu_total = record.preu_subtotal * (1 + record.percentatge_iva / 100)


