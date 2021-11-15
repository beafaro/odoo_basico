# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Exemplo de odoo basico'

    name = fields.Char(string="Título")
    descripcion = fields.Text(string="A descripción")
    alto = fields.Integer(string="Alto en centímetros")
    largo = fields.Integer(string="Largo en centímetros")
    ancho = fields.Integer(string="Ancho en centímetros")
    volumen = fields.Float(string="Volumen")
    peso = fields.Float(string="Peso en Kg's", default=2.7, digits=(6,2))
    densidad = fields.Float(string="Densidad")
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)

