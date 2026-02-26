# -*- coding: utf-8 -*-
{
    'name': "Asian Distributor Config",
    'summary': """
        Módulo base para empresa importadora y distribuidora asiática.
    """,
    'description': """
        Añade campos y procesos clave para importación, inventario, y ventas 
        en un entorno de distribución mayorista.
    """,
    'author': "Fairw",
    'category': 'Sales/Custom',
    'version': '18.0.1.0.0',
    'depends': ['sale_management', 'purchase', 'stock'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
