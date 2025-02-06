# -*- coding: utf-8 -*-
# from odoo import http


# class RegistreAlbarans(http.Controller):
#     @http.route('/registre_albarans/registre_albarans', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/registre_albarans/registre_albarans/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('registre_albarans.listing', {
#             'root': '/registre_albarans/registre_albarans',
#             'objects': http.request.env['registre_albarans.registre_albarans'].search([]),
#         })

#     @http.route('/registre_albarans/registre_albarans/objects/<model("registre_albarans.registre_albarans"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('registre_albarans.object', {
#             'object': obj
#         })

