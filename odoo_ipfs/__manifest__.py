{
    'name': "Blockchain Waves Synchro",
    'version': '1.0',
    'depends': ['base',
                'sale',
                'sales_team',
                'delivery',
                'barcodes',
                'mail',
                'report',
                'portal_sale',
                'website_portal',
                'website_payment',],
    'author': "Sergey Stepanets",
    'category': 'Application',
    'description': """
    Module for blockchain synchro
    """,
    'data': [
     'views/setting.xml',
     'data/cron.xml',
     'views/clients.xml',
     'views/sale_order.xml',
     'views/journal_signature.xml',
#     'views/report.xml',
    ],
}