from odoo import models,fields, api

class saga(models.Model):
    _name = 'examen.saga'
    name = fields.Char(string="Nombre Saga")
    videojuego_ids = fields.One2many("examen.videojuego", "saga_id", string="videojuegos")
    