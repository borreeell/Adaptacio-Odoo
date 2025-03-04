# -*- coding: utf-8 -*-
# from odoo import http


# class Factures(http.Controller):
#     @http.route('/factures/factures', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/factures/factures/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('factures.listing', {
#             'root': '/factures/factures',
#             'objects': http.request.env['factures.factures'].search([]),
#         })

#     @http.route('/factures/factures/objects/<model("factures.factures"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('factures.object', {
#             'object': obj
#         })

