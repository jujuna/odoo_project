from odoo import models, fields


class ParentDepartment(models.Model):
    _name = 'parent.department'
    _description = 'Parent of department'

    name = fields.Char(String='Name')