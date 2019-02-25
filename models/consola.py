from odoo import models,fields, api

class consola(models.Model):
    _name = 'examen.consola'
    name = fields.Char(string="Nombre Consola")
    videojuego_ids = fields.One2many("examen.videojuego", "consola_id", string="videojuegos")
    