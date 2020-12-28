# -*- coding: utf-8 -*-

from odoo import models, fields, api

class remorque(models.Model):
     _name = 'mon_parc.remorque'
     _rec_name = 'Immatriculatin'

     Immatriculatin = fields.Char('N° Immatriculation')
     NChassis = fields.Char('N° Chassis')
     VisiteTechnique = fields.Char('Visite echnique')
     AssuranceNational = fields.Char('Assurance National')
     AssuranceInternational = fields.Char('Assurance International')
     Pneumatique = fields.Char()
     Vidange = fields.Char()
     Vignette = fields.Char()
     Agrement = fields.Char()
     TachyGraphe = fields.Char()
     Extinteur = fields.Char()
     DisponibiliteRemorque = fields.Char('Disponibilite Remorque')
