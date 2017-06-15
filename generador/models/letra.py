from odoo import api, models, fields

class Letra(models.Model):

	_inherit = "res.partner"
	letter_pro = fields.Char(string="Letra")
