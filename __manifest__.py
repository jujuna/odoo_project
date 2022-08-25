# -*- coding: utf-8 -*-

{
    'name': 'Employee',
    'version': '1.0.0',
    'category': 'Employee_and_department',
    'description': """ Employee's ID card and department """,
    'sequence': -100,
    'depends': ['web'],
    'data': [
        'views/department.xml',
        'views/employee.xml',
        'views/feature.xml',
        'views/staytime.xml',
        'report/employee.xml',
        'report/employee_report.xml',
        'views/image.xml',
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',

    'assets': {
        'web.assets_backend': [
            'employee/static/src/js/gender_widget.js',
            'employee/static/src/scss/gender.css'
        ],
    },
}
