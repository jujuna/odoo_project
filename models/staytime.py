from odoo import models, fields


class StayTime(models.Model):
    _name = 'stay.time'
    _description = 'Time of coming and going'

    came = fields.Date(String='Came')
    went = fields.Date(String='Went')
    comment = fields.Char(String='Comment')
    employee = fields.Many2one(
        'employee.card', String='Stay time'
    )
