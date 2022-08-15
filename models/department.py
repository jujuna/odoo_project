from odoo import models, fields


class EmployeeDepartment(models.Model):
    _name = 'employee.department'
    _description = 'Departments'

    name = fields.Char(String='Name')
