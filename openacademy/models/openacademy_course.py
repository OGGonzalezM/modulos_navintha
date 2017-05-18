# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
    _name = 'openacademy.course'
    '#Nombre del modelo de odoo'

    '# field reserved to identify name record'

    name = fields.Char(string='Nombre', required=True)
    '#llave de la tabla, es como PK'

    '#string --> etiqueta de la variable name'

    description = fields.Text(string='Detalles', required=False)
    '#nombre del campo'
    responsible_id = fields.Many2one('res.users', ondelete='set null', string='Responsible', index=True)
