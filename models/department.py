from odoo import models, fields, api

class EmployeeDepartment(models.Model):
    _name = 'employee.department'
    _description = 'Departments'
    _rec_name = 'compute_name'

    name = fields.Char(String='Name')
    parent_department = fields.Many2one(
        'employee.department', String='Parent department'
    )
    compute_name = fields.Char(string='Name of object', compute='_compute_object_name')

    @api.depends('name', 'parent_department')
    def _compute_object_name(self):
        for field in self:
            if field.parent_department.name:
                field.compute_name = str(field.parent_department.compute_name) + ' / ' + str(field.name)
            else:
                field.compute_name = field.name
