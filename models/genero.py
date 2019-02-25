from odoo import models,fields, api

class genero(models.Model):
    _name = 'examen.genero'
    name = fields.Char(string="Nombre Genero")
    videojuego_ids = fields.One2many("examen.videojuego", "genero_id", string="videojuegos")
    