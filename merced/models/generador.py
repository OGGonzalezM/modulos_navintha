from odoo import api, exceptions, fields, models

class Generador(models.Model):
	_inherit = 'product.template'

	@api.multi
	def imprimir(self):
		prov_id = self.seller_ids.name
		#( name= id proveedor)
		ident_prov = prov_id.x_identificador
		print "***********************" +  str(ident_prov) + " ***********************"

		numero = 1000000000 + self.id
		print " * *** * " + str(numero) + " * *** * "
		num_str = str(numero)

		cod_barras = ident_prov + str(num_str[1:10])
		self.barcode = cod_barras