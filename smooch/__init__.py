import os
import json
import requests

SERVICE_URL = 'https://api.smooch.io'
app_token = os.environ['SMOOCH_APP_TOKEN']


class Smooch(object):

    def __init__(self, auth=None, service_url=SERVICE_URL):
        self.service_url = service_url

    def init(self, device, userId=None):
        payload = {
            'device': {
                'id': '7e6eedd677eb3ede0c636fc4c5b51a14',
                'platform': 'other'
            }
        }
        if (userId):
            payload['userId'] = userId

        headers = {'content-type': 'application/json',
                   'app-token': app_token}

        res = requests.post(self.service_url + '/v1/init',
                            data=json.dumps(payload), headers=headers)
        return res
