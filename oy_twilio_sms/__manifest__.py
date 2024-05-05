# -*- coding: utf-8 -*-
{
    'name': "Ouyuan Twilio SMS",

    'summary': """Send SMS by Twilio SMS Gateway, overwriting the default Odoo IAP SMS.""",

    'description': """
        This plugin is used to overwrite the Odoo default SMS IAP with the Twilio SMS.
    """,

    'author': "ryan",
    'website': "https://www.oyerp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hidden/Tools',
    'version': '16.0.1.0.0',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sms'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
    ],
}
