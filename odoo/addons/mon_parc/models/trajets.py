# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Trajet(models.Model):
    _name = 'mon_parc.trajet'
    _rec_name = 'trajet'
    

    trajet = fields.Char('Trajet',  required=True)
    detail = fields.Char('Détail',  required=True)


