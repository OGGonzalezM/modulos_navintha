# -*- coding: utf-8 -*-
from openerp import fields, models

class Relaciones_puestos(models.Model):
	_name = 'hr.responsabilidades'

	name = fields.Char(string="Descripcion")
	x_descripcionresponsabilidades = fields.Text(string="Frecuencia de realizacion")
