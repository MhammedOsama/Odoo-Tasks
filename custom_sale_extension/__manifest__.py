{
    'name': 'Custom Sale Extension',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Custom extension for Sales Orders',
    'description': 'Adds delivery note field and return policy to sales orders',
    'author': 'Your Company',
    'depends': ['sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'report/sale_order_report_templates.xml',
        'views/res_config_settings_views.xml',
    ],
    'installable': True,
    'application': True,
}

