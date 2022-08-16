# -*- coding: utf-8 -*-

{
    'name': 'Employee',
    'version': '1.0.0',
    'category': 'Employee_and_department',
    'description': """ Employee's ID card and department """,
    'sequence': -100,
    'depends': [],
    'data': [
        'views/department.xml',
        'views/Parentdepartment.xml',
        'views/employee.xml',
        'views/feature.xml',
        'views/staytime.xml',
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
