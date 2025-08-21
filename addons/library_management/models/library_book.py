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

    publisher_id = fields.Many2one(
        comodel_name='library.publisher',
        string='publisher'
    )

    genry_id = fields.Many2many(
         comodel_name='library.skill',
        relation='genre_skill_rel',
        column1='book_id',
        column2='genre_id',
        string='Genry'
    )

