from openerp import fields, models

class Navintha_employee_directory(models.Model):
	_inherit = 'res.partner'

	x_navintha_perfilacademico = fields.Char(string="Perfil academico")
	x_navintha_empleadoobservaciones = fields.Text(string="Observaciones")
	x_navintha_estudios = fields.One2many('hr.estudios_capacitaciones',
		 'x_navintha_estudios_name',
		  string="Estudios y capacitaciones")

