{
    "name": "My Library Management",
    "version": "1.0",
    "author": "Mikita",
    "category": "Library",
    "depends": ["base"],
    "data": [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_views.xml',
        'views/library_views_inherit.xml',
        'report/book_report.xml',
    ],
    "installable": True,
    "application": True,
}
