# -*- coding: utf-8 -*-

from odoo import models, fields, api

class chauffeur(models.Model):
     _name = 'mon_parc.chauffeur'
     _rec_name = 'nom'

     Immatricule = fields.Char('N° Immatricule')
     nom = fields.Char('Nom/Prenom')
     CIN = fields.Char('CIN')
     Npassport = fields.Char('N° de passport')
     Dateexpiration = fields.Char('Date D\'expiration')
     VisaDu = fields.Char('Visa Du')
     VisaAu = fields.Char('Visa Au')
     CNSS = fields.Char('CNSS')
     CDM = fields.Char('C D M')
     DateNaissance = fields.Char('Date de Naissance')
     NTelephoneMaroc = fields.Char('N° de Télephone Maroc')
     NTelephoneFrance = fields.Char('N° de Télephone France')
     NTelephoneEspagne = fields.Char('N° de Télephone Espagne')
     BadgeProvisoire = fields.Char('Badge Provisoire')
     BadgeDossier = fields.Char('Badge Dossier')
     Disponibilite = fields.Char('Disponibilité')