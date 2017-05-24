# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
    '# Openacademy == course'
    _name = 'openacademy.course'

    '# Nombre del modelo de odoo'
    '# field reserved to identify name record'
    name = fields.Char(string='Nombre', required=True)
    '#llave de la tabla, es como PK'

    '#string --> etiqueta de la variable name'

    description = fields.Text(string='Detalles', required=False)
    '#nombre del campo'
    responsible_id = fields.Many2one('res.users', ondelete='set null', string='Responsible', index=True)

    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
