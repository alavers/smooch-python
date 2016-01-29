import unittest2
from mock import patch, MagicMock, call
from smooch import Smooch
from smooch.resource import AppUser, Device

MOCK_INIT_RESPONSE = {
    'appUser': {
        '_id': 'apple',
        'signedUpAt': 'banana2',
        'conversationStarted': False,
        'properties': {}
    }
}

SAMPLE_DEVICE = Device('7e6eedd677eb3ede0c636fc4c5b51a14')
SAMPLE_APP_TOKEN = 'b057ef47ed438757278ce66072f5194a'
SAMPLE_JWT = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'


class InitTests(unittest2.TestCase):

    def setUp(self):
        super(InitTests, self).setUp()

        self.mock_session = MagicMock()

        mock_response = MagicMock()
        mock_response.json.return_value = MOCK_INIT_RESPONSE
        self.mock_session.post.return_value = mock_response

        self.session_patcher = patch('smooch.Session')
        mock_session_cls = self.session_patcher.start()
        mock_session_cls.return_value = self.mock_session
        self.addCleanup(self.session_patcher.stop)

    def test_defaults(self):
        res = Smooch(app_token=SAMPLE_APP_TOKEN).init(SAMPLE_DEVICE)
        self.mock_session.post.assert_called_once()

    def test_app_token(self):
        Smooch(app_token=SAMPLE_APP_TOKEN).init(SAMPLE_DEVICE)
        self.mock_session.headers.update.assert_has_calls(
            call({'app-token': SAMPLE_APP_TOKEN}))

    def test_jwt(self):
        Smooch(jwt=SAMPLE_JWT).init(SAMPLE_DEVICE)
        self.mock_session.headers.update.assert_has_calls(
            call({'authorization': 'Bearer ' + SAMPLE_JWT}))

if __name__ == '__main__':
    unittest2.main()
