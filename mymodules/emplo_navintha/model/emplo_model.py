#-*- coding_ utf-8 -*-
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from openerp import api, fields, models

class emplo_navintha(models.Model):

    _inherit = 'hr.employee'

    x_numempleado = fields.Char(string="Numero de Empleado")
    x_contratacion = fields.Datetime(string="Fecha de Contratacion")
    x_antiguedad = fields.Char(string="Antiguedad", readonly=True, compute='_total_minutes')
    x_observaciones = fields.Text(string="Observaciones")
    x_fechaactual = fields.Datetime(default=fields.Datetime.now)
    x_perfilacademico = fields.Many2one('hr.escolaridad', string="Perfil Academico")
    #Campos para los documentos
    x_navintha_documentos_actanacimiento = fields.Boolean(string="Acta de nacimiento")
    #x_navintha_documentos
    x_navintha_documentos_ine = fields.Boolean(string="INE")
    x_navintha_documentos_comprobantedomicilio = fields.Boolean(string="Comprobante de domicilio")
    x_navintha_documentos_curp = fields.Boolean(string="CURP")
    x_navintha_documentos_cv = fields.Boolean(string="Curriculum Vitae")
    x_navintha_documentos_comprobanteestudios = fields.Boolean(string="Comprobante de estudios")

    @api.one
    @api.depends('x_contratacion','x_fechaactual')
    def _total_minutes(self):
        if self.x_contratacion and self.x_fechaactual:
            start_dt = fields.Datetime.from_string(self.x_contratacion)
            finish_dt = fields.Datetime.from_string(self.x_fechaactual)
            difference = relativedelta(finish_dt, start_dt)
            year = difference.years
            month = difference.months
            days = difference.days
            self.x_antiguedad = str(year)+" anios "+str(month)+" meses "+str(days)+" dias"
        return {}
