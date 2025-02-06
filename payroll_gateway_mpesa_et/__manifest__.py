{
    'name': "Safaricom ET salary payment orchestrator",
    'version': '14.0',
    'depends': ['payroll', 'payroll_gateway'],
    'author': "TREVI Software",
    'category': "Payroll",
    'description': """
        Make salary payments through Safaricom Ethiopia's payment gateway.
    """,
    'data': [
        "views/hr_employee_view.xml",
        "views/hr_payslip_view.xml",
        "views/payroll_gateway_mpesa_et_view.xml"
    ]
}