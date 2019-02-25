from odoo import models,fields, api

class videojuego(models.Model):
    _name = 'examen.videojuego'
    nombrePortada = fields.Char(string="nombre")
    precio = fields.Char(string="asignatura")
    numeroUnidades = fields.Char(string="profesor")
    dineroGenerado = fields.Many2one("colegio.colegio", string="colegio")
    estudiante_ids = fields.One2many("colegio.estudiante", "clase_id", string="estudiantes")


    @api.one
    def generate_record_name(self):
        self.name = 'aleatorio'

