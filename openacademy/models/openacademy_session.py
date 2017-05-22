#Fijarse bien en las importaciones.
from odoo import api, fields, models


class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help='Duration in days')
    seats = fields.Integer(string='Numero de asientos')

    instructor_id = fields.Many2one('res.partner', string='Instructor',
        domain=['|', ('instructor', '=', True),
        ('category_id.name', 'ilike', 'Teacher')])

    course_id = fields.Many2one('openacademy.course', ondelete='cascade',
        string='Course', required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    taken_seats = fields.Float(string="Taken Seats", compute='_taken_seats')

    @api.one
    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        #if not hace referencia a nada, es decir, null, cero, etc.
        if not self.seats:
            self.seats = 0.0
        else:
            self.taken_seats = 100.0 * len(self.attendee_ids) / self.seats
