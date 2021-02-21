# -*- coding: utf-8 -*-
{
    'name': "Quotation_discount",

    'summary': """
        add in Quotations
        discount fields
         """,

    'description': """
        add in Quotations
        discount value field
        before discount field
        total discount field
    """,

    'author': "kerols ayed",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
