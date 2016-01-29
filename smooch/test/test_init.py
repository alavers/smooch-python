import unittest2
from mock import patch, Mock
from smooch import Smooch
from smooch.resource import AppUser, Device


class InitTests(unittest2.TestCase):

    def test_defaults(self):
        res = Smooch().init(Device('7e6eedd677eb3ede0c636fc4c5b51a14'))
        print res._id

if __name__ == '__main__':
    unittest2.main()
