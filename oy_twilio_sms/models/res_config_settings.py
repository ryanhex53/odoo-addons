from odoo import fields, models


class ResConfigSettings(models.TransientModel):
  _inherit = 'res.config.settings'

  twilio_enabeld = fields.Boolean(string='Twilio Enabled', config_parameter='oy_twilio_sms.enabeld')
  twilio_account_sid = fields.Char(string='Account SID', config_parameter='oy_twilio_sms.account_sid')
  twilio_auth_token = fields.Char(string='Auth Token', config_parameter='oy_twilio_sms.auth_token')
  twilio_number = fields.Char(string='Twilio Number', config_parameter='oy_twilio_sms.number')