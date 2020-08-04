{
    'name': 'Library Management',
    'description': 'Manage library book catalogue and lending.',
    'author': 'Mahmoud Rhazzoul',
    'depends': ['base'],
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/book_list_template.xml',
    ],
    'application': True,
}
