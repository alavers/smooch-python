import json
import requests
from requests import Session
from smooch.resource import AppUser, Device

SERVICE_URL = 'https://api.smooch.io'


class Smooch(object):

    def __init__(self, jwt=None, app_token=None, service_url=SERVICE_URL):
        if jwt and app_token:
            raise ValueError(
                'Only jwt or app_token may be specified, not both')

        if not (jwt or app_token):
            raise ValueError('jwt or app_token must be specified')

        self.s = Session()
        self.s.headers.update({'content-type': 'application/json'})
        if jwt:
            self.s.headers.update({'authorization': 'Bearer ' + jwt})
        else:
            self.s.headers.update({'app-token': app_token})

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

        res = self.s.post(self.service_url + '/v1/init',
                          data=json.dumps(payload))
        return AppUser(res.json()['appUser'])
