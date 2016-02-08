from requests import Session


class Api(object):

    def __init__(self, service_url, jwt=None, app_token=None):
        if jwt and app_token:
            raise ValueError(
                'Only jwt or app_token may be specified, not both')

        if not (jwt or app_token):
            raise ValueError('jwt or app_token must be specified')

        self._session = Session()
        self._session.headers.update({'content-type': 'application/json'})
        if jwt:
            self._session.headers.update({'authorization': 'Bearer ' + jwt})
        else:
            self._session.headers.update({'app-token': app_token})

        self._base = service_url + '/v1'

    def get(self, path):
        return self._session.get(self._base + path)

    def post(self, path, data):
        return self._session.post(self._base + path, data)
