import os
import json
import requests
from smooch.resource import AppUser, Device

SERVICE_URL = 'https://api.smooch.io'
app_token = os.environ['SMOOCH_APP_TOKEN']


class Smooch(object):

    def __init__(self, auth=None, service_url=SERVICE_URL):
        self.service_url = service_url

    def init(self, device, userId=None):
        payload = {
            'device': {
                'id': device.id,
                'platform': device.platform
            }
        }
        if (userId):
            payload['userId'] = userId

        headers = {'content-type': 'application/json',
                   'app-token': app_token}

        res = requests.post(self.service_url + '/v1/init',
                            data=json.dumps(payload), headers=headers)
        return AppUser(res.json()['appUser'])
