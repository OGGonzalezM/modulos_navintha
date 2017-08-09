#-*- coding:UTF-8 -*-
from openerp import models, fields

class Estudios(models.Model):

    _name = 'estudios.hr'

    name = fields.Char()
    x_fechainicio = fields.Date(string="Fecha de Inicio")
    x_fechafin = fields.Date(string="Fecha de Fin")
    x_descripcion = fields.Text(string="Descripcion")
    x_nivel = fields.Char(string="Nivel")
    x_institucion = fields.Char(string="Institucion")
