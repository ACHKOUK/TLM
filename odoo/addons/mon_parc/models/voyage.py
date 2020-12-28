# -*- coding: utf-8 -*-

from logging import log
from odoo.tools.misc import logged
from odoo import models, fields, api


class voyage(models.Model):
    _name = 'mon_parc.voyage'

    datedepart = fields.Date('date de départ')
    datearrivee = fields.Date('Date Date d\'échéance')
    pointdepart = fields.Char('point de depart')
    pointarrivee = fields.Char('point d\'arrivée')
    ndossier =fields.Char('N° Dossier')
    commentaire =fields.Char('Commentaire')
    factureid =fields.Char('N° Facture')
    Avance =fields.Char('Avance')
    reste =fields.Char('Le reste')
    typevoyage = fields.Selection([('import', 'import'),('export', 'export')])

    tracteur_id = fields.Many2one(comodel_name='mon_parc.tracteur')
    remorque_id = fields.Many2one(comodel_name='fleet.vehicle')
    chauffeur_id = fields.Many2one(comodel_name='hr.employee',domain="[('department_id' , '=', 6)]")
    chauffeur2_id = fields.Many2one(comodel_name='hr.employee',domain="[('department_id' , '=', 6)]")
    client_id = fields.Many2one(comodel_name='res.partner', string='Client', required=True, domain="[('customer_rank' , '=', 1)]")
    trajets_id = fields.Many2one(comodel_name='mon_parc.trajet')
    mession_id = fields.Many2one(comodel_name='fleet.vehicle.mission')

    @api.model
    def create(self, vals):
        rec = super(voyage, self).create(vals)
        # if not rec.remorque_id:
        rec._update_statut_vehicule()
        return rec

    
    def _create_check_sequence(self):
        """ Create a check sequence for the journal """
        self.mession_id = self.env['fleet.vehicle.mission'].sudo().create({
            'comment': 'yyyyyy',
            'date_sortie': self.datedepart,
            'date_arrivee': 'yyy',
            'vehicle_id':self.remorque_id.id,
        })


    def _update_statut_vehicule(self):
        """
        update statu vehicule to en mession
        """
        self.env['fleet.vehicle'].search([
            ('id', '=', self.remorque_id.id),
        ]).write({'state_id':7})