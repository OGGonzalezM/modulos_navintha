from odoo import api, fields, models


class Region(models.Model):
	_inherit = 'res.partner'
	x_region = fields.Char(string="Regiones123", compute='_cambio_region')


	@api.one
	@api.depends('state_id.code')
	def _cambio_region(self):
		print " * ************************ Depurando codigo **********************"
		for record in self:
		    centrosur = ['PUE', 'TLAX', 'HGO', 'OAx', 'VER']
		    centro = ['GRO', 'MOR', 'DF', 'MEX']
		    sureste = ['CAMP', 'CHIS', 'Q ROO', 'TAB', 'YUC']
		    bajio = ['GTO', 'JAL', 'MICH', 'QRO', 'SLP', 'AGS', 'COL', 'NAY', 'ZAC']
		    norte = ['COAH', 'NL', 'TAMPS']
		    noreste = ['SIN', 'DGO', 'CHIH', 'SON']
		    bc = ['BCS', 'BC']
		    estado = self.state_id.code
		    if estado in centrosur:
		        print " Centro - sur **********************"
		        record['x_region'] = 'Centro-Sur'
		    elif estado in centro:
		    	print " Centro ********************************"
		        record['x_region'] = 'Centro'
		    elif estado in sureste:
		    	print " Sureste **************************"
		        record['x_region'] = 'Sureste'
		    elif estado in bajio:
		    	print " Bajio **********************************"
		        record['x_region'] = 'Bajio'
		    elif estado in norte:
		    	print " Norte *******************************************"
		        record['x_region'] = 'Norte'
		    elif estado in noreste:
		    	print " Noreste *******************************************"
		        record['x_region'] = 'Noreste'           
		    elif estado in bc:
		    	print " Baja calidfornia *******************************************"
		        record['x_region'] = 'Baja California'
