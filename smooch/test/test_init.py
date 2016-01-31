import unittest2
from mock import patch, MagicMock, call
from smooch import Smooch
from smooch.resource import AppUser, Device
from smooch.test.sample import INIT_RESPONSE, DEVICE, JWT, APP_TOKEN


class InitTests(unittest2.TestCase):

    def setUp(self):
        super(InitTests, self).setUp()

        self.mock_session = MagicMock()

        mock_response = MagicMock()
        mock_response.json.return_value = INIT_RESPONSE
        self.mock_session.post.return_value = mock_response

        self.session_patcher = patch('smooch.Session')
        mock_session_cls = self.session_patcher.start()
        mock_session_cls.return_value = self.mock_session
        self.addCleanup(self.session_patcher.stop)

    def test_defaults(self):
        res = Smooch(app_token=APP_TOKEN).init(DEVICE)
        self.mock_session.post.assert_called_once()

    def test_app_token(self):
        Smooch(app_token=APP_TOKEN).init(DEVICE)
        self.mock_session.headers.update.assert_has_calls(
            call({'app-token': APP_TOKEN}))

    def test_jwt(self):
        Smooch(jwt=JWT).init(DEVICE)
        self.mock_session.headers.update.assert_has_calls(
            call({'authorization': 'Bearer ' + JWT}))

if __name__ == '__main__':
    unittest2.main()
