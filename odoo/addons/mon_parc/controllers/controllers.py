# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
     @http.route('/mon_parc/mon_parc/', auth='public')
     def index(self, **kw):
         return "Hello, world"

     @http.route('/mon_parc/mon_parc/objects/', auth='public')
     def list(self, **kw):
         return http.request.render('mon_parc.listing', {
             'root': '/mon_parc/mon_parc',
             'objects': http.request.env['mon_parc.mon_parc'].search([]),
         })

     @http.route('/mon_parc/mon_parc/objects/<model("mon_parc.mon_parc"):obj>/', auth='public')
     def object(self, obj, **kw):
         return http.request.render('mon_parc.object', {
             'object': obj
         })