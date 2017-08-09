# -*- coding: utf-8 -*-
from openerp import fields, models

class Navintha_datosempresa(models.Model):
    _inherit = "res.company"

    x_navintha_mision = fields.Text(string="Misión")
    x_navintha_vision = fields.Text(string="Visión")
    x_navintha_valores = fields.Text(string="Valores")
    x_navintha_politicadecalidad = fields.Text(string="Política de Calidad")
    x_navintha_objetivosdecalidad = fields.Text(string="Objetivos de Calidad")
