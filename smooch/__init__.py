import json
from smooch.api import Api
from smooch.error import SmoochError
from smooch.resource import (  # noqa
    AppUser,
    Device,
    Conversation,
    Message
)

SERVICE_URL = 'https://api.smooch.io'


class Smooch(object):

    def __init__(self, service_url=SERVICE_URL, jwt=None, app_token=None):
        self._api = Api(service_url, jwt, app_token)

    def init(self, device, userId=None):
        payload = {
            'device': device.dict()
        }

        if (userId):
            payload['userId'] = userId

        res = self._api.post('/init', data=json.dumps(payload))

        if (res.status_code != 200):
            raise SmoochError('Init failed', res)

        app_user = AppUser(api=self._api, **res.json()['appUser'])
        return app_user
