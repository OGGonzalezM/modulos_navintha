from odoo import api, fields, models


class Trust(models.Model):
	_inherit = 'res.partner'
	x_cmt_trust = fields.Integer(compute='_get_trust')

	@api.one
	@api.depends('x_cmt_tambienconstruye',
		 'x_cmt_instalauidmismo',
		 'x_cmt_cuentaconpersonal',
		 'x_cmt_solovendeotmbninstala',
		 'x_cmt_quetipodebienes',)
	def _get_trust(self):
	    for record in self:
    		record['x_cmt_trust'] = self.x_cmt_tambienconstruye + self.x_cmt_instalauidmismo + self.x_cmt_cuentaconpersonal + self.x_cmt_solovendeotmbninstala + self.x_cmt_quetipodebienes
