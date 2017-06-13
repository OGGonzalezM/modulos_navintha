from odoo import api, models, fields

class Generador(models.Model): 
    _inherit = 'product.template'

    #cod_barras = fields.Char(string="Codigo", readonly=True)
    proveedor_id = fields.Many2one('res.partner', string="Proveedor")

    #General codigo de barras
    @api.multi
    def gen_codigos(self):
        nom_proveedor = self.proveedor_id.name
        longitud = len(nom_proveedor)
        prefijo = nom_proveedor[0]
        numero = 1000000000 + self.id
        num_str = str(numero)
        #self.cod_barras = prefijo + str(num_str[1:10])
        self.barcode = prefijo + str(num_str[1:10])
