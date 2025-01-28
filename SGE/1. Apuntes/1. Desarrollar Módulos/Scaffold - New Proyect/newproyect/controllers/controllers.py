# -*- coding: utf-8 -*-
# from odoo import http


# class Newproyect(http.Controller):
#     @http.route('/newproyect/newproyect/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/newproyect/newproyect/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('newproyect.listing', {
#             'root': '/newproyect/newproyect',
#             'objects': http.request.env['newproyect.newproyect'].search([]),
#         })

#     @http.route('/newproyect/newproyect/objects/<model("newproyect.newproyect"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('newproyect.object', {
#             'object': obj
#         })
