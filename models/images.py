from odoo import models, fields


class Images(models.Model):
    _name = 'images.upload'

    image = fields.Image(String='Image')
    description = fields.Char(String='Description')


