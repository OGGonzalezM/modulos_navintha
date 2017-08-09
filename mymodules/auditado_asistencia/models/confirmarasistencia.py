from openerp import fields, models

class Confirmarasistencia(models.Model):
	_inherit = 'res.users'

	confirmar_asistencia = fields.Boolean(string="Confirmar asistencia")