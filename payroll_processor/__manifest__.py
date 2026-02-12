{
    'name': "Default Payroll Gateway",
    'version': '14.0',
    'depends': ['payroll'],
    'author': "TREVI Software",
    'category': "Payroll",
    'description': """
        Make salary payments through a payment gateway.
    """,
    'data': [
        "views/menus.xml",
        "views/hr_employee_view.xml",
        "views/hr_payslip_view.xml",
        "views/res_config_settings_view.xml",
    ],
    'post_init_hook': 'post_init_hook',
}