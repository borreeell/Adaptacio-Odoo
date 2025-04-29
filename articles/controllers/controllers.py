# -*- coding: utf-8 -*-
# from odoo import http


# class Articles(http.Controller):
#     @http.route('/articles/articles', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/articles/articles/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('articles.listing', {
#             'root': '/articles/articles',
#             'objects': http.request.env['articles.articles'].search([]),
#         })

#     @http.route('/articles/articles/objects/<model("articles.articles"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('articles.object', {
#             'object': obj
#         })

