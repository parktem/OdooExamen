from odoo import models,fields, api

class videojuego(models.Model):
    _name = 'examen.videojuego'
    name = fields.Char(string="Nombre Portada")
    precio = fields.Integer(string="Precio")
    numeroUnidades = fields.Integer(string="Numero Unidades")
    dineroGenerado = fields.Integer(string="Dinero Generado")
    capturas = fields.Boolean(string="Capturas")
    saga_id = fields.Many2one("examen.saga", string="Saga")
    compania_id = fields.Many2one("base.empresa", string="Compania")
    genero_id = fields.Many2one("examen.genero", string="Genero")
    consola_id = fields.Many2one("examen.consola", string="Consola")


    @api.one
    def modificarCaptura(self):
        self.capturas = not self.capturas


    @api.onchange('numeroUnidades', 'precio')
    def calcular_dinero(self):
        self.dineroGenerado = self.numeroUnidades * self.precio 

