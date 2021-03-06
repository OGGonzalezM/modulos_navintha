# -*- coding: utf-8 -*-

#Por convencion se ponen en orden alfabetico
from odoo import api, models, fields, _


class Course(models.Model):
    '# Openacademy == course'
    _name = 'openacademy.course'

    '# Nombre del modelo de odoo'
    '# field reserved to identify name record'
    name = fields.Char(string='Nombre', required=True)
    '#llave de la tabla, es como PK'

    '#string --> etiqueta de las variables'

    description = fields.Text(string='Detalles', required=False)
    '#nombre del campo'
    responsible_id = fields.Many2one('res.users', ondelete='set null', string='Responsible', index=True)

    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         _("The title of the course should not be the description")),

        ('name_unique',
         'UNIQUE(name)',
         _("The course title must be unique")),
    ] 

    @api.multi
    #api one send default params cr, uid, id, context
    def copy(self, default=None):
        #default['name'] = self.name + ' (copy)'
        copied_count = self.search_count([('name', '=like', _(u"Copy of {}%").format(self.name))])
        if not copied_count:
            new_name = _(u"Copy of {}%").format(self.name)
        else:
            new_name = _(u"Copy of {} ({})").format(self.name, copied_count)
        default['name'] = new_name
        return super(Course, self).copy(default)

#AttributeError: 'list' object has no attribute 'id'
