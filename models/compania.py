from odoo import models,fields, api

class compania(models.Model):
    _name = 'examen.compania'
    name = fields.Char(string="Nombre Compania")
    videojuego_ids = fields.One2many("examen.videojuego", "compania_id", string="videojuegos")
    