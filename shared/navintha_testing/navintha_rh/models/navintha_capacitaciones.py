from openerp import fields, models

class Estudios_capacitaciones(models.Model):
	_name = 'hr.estudios_capacitaciones'

        x_navintha_estudios_name = fields.Char(string="Nombre")
	x_navintha_estudios_descripcion = fields.Text(string="Descripcion")
	x_navintha_nivel = fields.Char(string="Nivel")
	x_navintha_institucion = fields.Char(string="Institucion")
	x_navintha_estudios_fechainicio = fields.Date(string="Fecha de inicio")
	x_navintha_estudios_fechafin = fields.Date(string="Fecha fin")
        x_navintha_estudios_personal = fields.Many2one('res.partner', string="Personal")

