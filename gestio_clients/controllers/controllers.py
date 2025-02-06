# -*- coding: utf-8 -*-
# from odoo import http


# class GestioClients(http.Controller):
#     @http.route('/gestio_clients/gestio_clients', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestio_clients/gestio_clients/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestio_clients.listing', {
#             'root': '/gestio_clients/gestio_clients',
#             'objects': http.request.env['gestio_clients.gestio_clients'].search([]),
#         })

#     @http.route('/gestio_clients/gestio_clients/objects/<model("gestio_clients.gestio_clients"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestio_clients.object', {
#             'object': obj
#         })

