from odoo import models, fields


class EmployeeFeatue(models.Model):
    _name = 'employee.feature'
    _description = 'Features of employee'

    name = fields.Char(String='Name')
