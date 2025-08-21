from odoo import models, fields

class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"

    name = fields.Char("name")
    year = fields.Integer("year")