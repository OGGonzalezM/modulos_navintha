from odoo import api, fields, models

class Perfilconfirmado(models.Model):
	_inherit = 'res.partner'
	x_perfilconfirmado = fields.Text(string="Perfil del cliente", compute='_fijar_perfil_cliente')

	@api.one
	@api.depends('x_cmt_cualessuactividadprincipal',
		 'x_cmt_tambienconstruye',
		 'x_cmt_cuentaconpersonalproftec',
		 'x_cmt_subcontrata', 
		 'x_cmt_solovendeotmbninstala', 
		 'x_cmt_quetipodebienes', 
		 'x_cmt_distribuyepanel',
		 'x_contr_distripanel', 
		 'x_contr_cuentacnpersonal', 
		 'x_cmt_instalacionesfabriles')
	def _fijar_perfil_cliente(self):
		for record in self:
		# Proyectista
		    if (self.x_cmt_cualessuactividadprincipal == 30):
		        if (self.x_cmt_tambienconstruye == 30):
		            record['x_perfilconfirmado'] = "Proyectista"
		        elif (self.x_cmt_tambienconstruye == 10):
		            record['x_perfilconfirmado'] = "Contratista"
		        else:
		            record['x_perfilconfirmado'] = "Ninguno"
		# Profesional Tecnico            
		    elif (self.x_cmt_cualessuactividadprincipal == 20):
		        if (self.x_cmt_cuentaconpersonalproftec == 10):
		            if (self.x_cmt_distribuyepanel == True):
		                record['x_perfilconfirmado'] = "Profesional Tecnico"
		            elif (self.x_cmt_cuentaconpersonalproftec == 20 and self.x_cmt_distribuyepanel == True):
		                record['x_perfilconfirmado'] = "Contratista"
		        elif (self.x_cmt_cuentaconpersonalproftec == 20 and self.x_cmt_distribuyepanel == True):
		            record['x_perfilconfirmado'] = "Contratista"
		        else:
		            record['x_perfilconfirmado'] = "Ninguno"
		# Contratista
		    elif (self.x_cmt_cualessuactividadprincipal == 40):
		        if (self.x_contr_cuentacnpersonal == 3):
		            if (self.x_contr_distripanel == True):
		                record['x_perfilconfirmado'] = "Contratista"
		            else:
		                record['x_perfilconfirmado'] = "Profesional Tecnico"    
		        else:
		            record['x_perfilconfirmado'] = "Profesional Tecnico"
		# Distribuidor
		    elif (self.x_cmt_cualessuactividadprincipal == 60):
		        if (self.x_cmt_solovendeotmbninstala == 60):
		            record['x_perfilconfirmado'] = "Distribuidor"
		        elif (self.x_cmt_solovendeotmbninstala == 10):
		            record['x_perfilconfirmado'] = "Contratista"
		        else:
		            record['x_perfilconfirmado'] = "Ninguno"
		# Fabricante
		    elif (self.x_cmt_cualessuactividadprincipal == 70):
		        if (self.x_cmt_quetipodebienes == 70):
		            if (self.x_cmt_instalacionesfabriles == True):
		                record['x_perfilconfirmado'] = "Fabricante"
		            else:
		                record['x_perfilconfirmado'] = "Distribuidor"
		    else:
		        record['x_perfilconfirmado'] = "Ninguno"