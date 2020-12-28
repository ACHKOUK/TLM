# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tracteur(models.Model):
     _name = 'mon_parc.tracteur'
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
     Disponibilitetracteur = fields.Char('Disponibilite Tracteur')
     CodeSecretAS24 = fields.Char('Code Secret AS24')
     CodeSecretTRAFIC = fields.Char('Code Secret TRAFIC')