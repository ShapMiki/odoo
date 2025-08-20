from odoo import models, fields

class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"

    title = fields.Char("Title", required=True)
    author = fields.Char("Author")
    isbn = fields.Char("ISBN")
    description = fields.Text("Description")
    published_date = fields.Date("Published Date")
    is_available = fields.Boolean("Is Available", default=True)