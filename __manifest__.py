{
    "name": "Technical Support Ticket",
    "version" : "1.0",
    "author" : "vinhcodeacademy@gmail.com",
    "description": """
     Technical Support Ticket module to show available properties
    """,
    "category": "Sales",
    "depends": ['CanhCamBase','Hosting','mail'],
    "data": [

        'security/ir.model.access.csv',
        'security/res._groups.xml',
        'security/model_access.xml',
        'security/ir_rule.xml',
                  
        'views/ticket_view.xml',
        'views/ticket_type_view.xml',
        'views/ticket_status_view.xml',
        'views/ticket_respone_view.xml',
        'views/menu_items.xml',

        'data/mail_template.xml',

    ],
    "installable" : True,
    "application" : True,
    "license" : "LGPL-3",
    'auto_install': False,
}