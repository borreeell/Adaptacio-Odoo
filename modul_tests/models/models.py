

from odoo import models, fields, api


class modul_tests(models.Model):
    _name = 'modul_tests.modul_tests'
    _description = 'modul_tests.modul_tests'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    field1 = fields.Char(string="field")