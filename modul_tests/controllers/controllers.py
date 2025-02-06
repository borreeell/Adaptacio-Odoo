# -*- coding: utf-8 -*-
# from odoo import http


# class ModulTests(http.Controller):
#     @http.route('/modul_tests/modul_tests', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modul_tests/modul_tests/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modul_tests.listing', {
#             'root': '/modul_tests/modul_tests',
#             'objects': http.request.env['modul_tests.modul_tests'].search([]),
#         })

#     @http.route('/modul_tests/modul_tests/objects/<model("modul_tests.modul_tests"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modul_tests.object', {
#             'object': obj
#         })

