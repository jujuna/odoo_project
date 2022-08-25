from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re


class Employee(models.Model):
    _name = 'employee.card'
    _description = 'Employee information'
    _rec_name = 'first_name'

    test = fields.Integer()
    first_name = fields.Char(String='First name')
    last_name = fields.Char(String='Last name')
    citizenship = fields.Char(String='Citizenship')
    gender = fields.Selection(
        [('Male', 'Male'), ('Female', 'Female')], String='My Selection Field')
    personal_id = fields.Char(String='Personal id')
    date_of_birth = fields.Date(string='Date of birth')
    date_of_expiry = fields.Date(string='Date of expiry')
    place_of_birth = fields.Char(String='Place of birth')
    date_of_issue = fields.Date(String='Date of issue')
    image = fields.Image(String='image')
    department = fields.Many2one('employee.department', String='Department')
    features = fields.Many2many(comodel_name='employee.feature', inverse_name='employee', String='Department')
    stay_time = fields.One2many(comodel_name='stay.time', inverse_name='employee', String='Stay time')

    @api.constrains('personal_id')
    def _check_id(self):
        for record in self:
            if re.match("^\d{11}", record.personal_id) is None:
                raise ValidationError("ID must be 11 digit")