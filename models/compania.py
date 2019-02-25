from odoo import models,fields, api

class compania(models.Model):
    _inherit = 'base.empresa'
    name = fields.Char(string="Nombre Compania")
    videojuego_ids = fields.One2many("examen.videojuego", "compania_id", string="videojuegos")
    
