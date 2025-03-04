from odoo import models, fields, api
from odoo.exceptions import UserError
import re


class GestioClients(models.Model):
    _name = 'gestio_clients.gestio_clients'
    _description = 'Gestio Clients'

    individual = fields.Boolean(string='Individual', default = False)
    empresa = fields.Boolean(string='Empresa')
    id_client = fields.Char(string='ID del client')  
    nom_client = fields.Char(string='Nom del client: ')
    adreca = fields.Char(string='Adreça del client: ')
    codi_postal = fields.Integer(string='Codi postal: ')
    localitat = fields.Char(string='Localitat: ')
    telefon = fields.Integer(string='Telefon: ')
    mail = fields.Char(string='Mail: ')
    nif = fields.Char(string='NIF: ')


    @api.model
    def create(self, vals):
        if 'id_client' not in vals or not vals['id_client']:
            # Crida al metode next_by_code del model ir.sequence
            vals['id_client'] = self.env['ir.sequence'].next_by_code('gestio.clients.sequence') or '/'
        return super(GestioClients, self).create(vals)

    @api.onchange('individual', 'empresa')
    def _onchange_individual_empresa(self):
        self.individual = not (self.empresa) # Desmarca empresa si esta marcada
        self.empresa = not (self.individual) # Desmarca individual si esta marcada
    
    @api.constrains('nif', 'empresa', 'individual')
    def _comprova_nif(self):
        for record in self:
            if record.empresa and record.nif:
                if not re.match(r'^[A-Za-z]', record.nif):
                    raise UserError("El NIF d'una empresa ha de començar amb una lletra")
            elif record.individual and record.nif:
                if not re.match(r'^[A-Za-z]$', record.nif):
                    raise UserError("El NIF d'un particular ha d'acabar amb una lletra")

    
