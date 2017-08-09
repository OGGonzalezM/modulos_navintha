from openerp import fields, models

class Auditorias_campos(models.Model):
	_inherit = 'mgmtsystem.audit'

	x_indexol_auditoriafin = fields.Date(string="Fecha fin")
	x_indexol_tipoauditoria = fields.Selection(string="Tipo de auditoria", selection=[('Interna', 'Interna'),('Externa','Externa')])
	x_indexol_confirmarasistencia = fields.Boolean(string="Confirmar asistencia")