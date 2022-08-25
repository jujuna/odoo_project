from odoo import models, fields


class ImagesGallery(models.Model):
    _name = 'images.gallery'

    image = fields.Many2many(comodel_name='ir.attachment', string='Images')

