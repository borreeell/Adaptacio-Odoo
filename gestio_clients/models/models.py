# Module: gestio_clients
# Descripcio: Aquest modul defineix els models per gestionar els clients individuals i empreses a Odoo.
# Classes:
#   GestioClients (Registre de les dades del client):
#      - individual: Checkbox per marcar si el client es individual.
#      - empresa: Checkbox per marcar si el client es una empresa.
#      - id_client: Identificador unic per el client.
#      - nom_client: Nom del client.
#      - adreca: Adreça del client.
#      - codi_postal: Codi postal de la localitat del client.
#      - localitat: Localitat del client.
#      - telefon: Telefon de contacte del client.
#      - mail: Correu electronic del client.
#      - nif: NIF del client.
# Metodes:
#   - create(self, vals):
#       Crea un identificador unic per el client si no s'ha proporcionat.
#   - _onchange_individual_empresa(self):
#       Desmarca la contraria si una de les dues opcions esta marcada.



from odoo import models, fields, api


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
