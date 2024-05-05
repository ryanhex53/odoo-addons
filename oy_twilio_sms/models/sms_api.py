# -*- coding: utf-8 -*-

import concurrent.futures
import logging

import requests

from odoo import api, models

_logger = logging.getLogger(__name__)


class SmsApi(models.AbstractModel):
  _inherit = 'sms.api'

  @api.model
  def _contact_iap(self, local_endpoint, params):
    if local_endpoint == '/iap/message_send':
      """
      Send a single message to several numbers
      """
      _logger.info('Sending Single SMS using IAP %s', params)
      return super(SmsApi, self)._contact_iap(local_endpoint, params)
    elif local_endpoint == '/iap/sms/2/send':
      """
      Send SMS using IAP in batch mode
      """
      config = self.env['ir.config_parameter'].sudo()
      if config.get_param('oy_twilio_sms.enabeld', False):
        _logger.info('Sending Batch SMS using Twilio %s', params)
        account_sid = config.get_param('oy_twilio_sms.account_sid')
        auth_token = config.get_param('oy_twilio_sms.auth_token')
        number = config.get_param('oy_twilio_sms.number')
        url = 'https://api.twilio.com/2010-04-01/Accounts/%s/Messages.json' % account_sid
        headers = {
          'Content-Type': 'application/x-www-form-urlencoded',
        }
        # 并发发送短信
        results = []
        with concurrent.futures.ThreadPoolExecutor() as executor:
          futures = []
          for message in params['messages']:
            data = {
              'From': number,
              'To': message['number'],
              'Body': message['content'],
            }
            future = executor.submit(requests.post, url, headers=headers, data=data, auth=(account_sid, auth_token))
            futures.append(future)

          for future, message in zip(futures, params['messages']):
            res = future.result()
            body = res.json()
            results.append({
              'res_id': message['res_id'],
              'state': 'success' if res.status_code == 201 else 'server_error',
              'credit': body.get('num_segments', 0)
            })
            if res.status_code != 201:
              _logger.error('Failed to send SMS: %s', body['message'])

        return results
      else:
        return super(SmsApi, self)._contact_iap(local_endpoint, params)
