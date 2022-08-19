from odoo import models, fields


class EmployeeFeatue(models.Model):
    _name = 'employee.feature'
    _description = 'Features of employee'
    _rec_name = 'name'

    name = fields.Char(String='Name')
    employee = fields.Many2one(
        'employee.card', String='Employee'
    )
