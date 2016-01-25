from smooch import Smooch
import unittest2


class InitTests(unittest2.TestCase):

    def test_defaults(self):
        res = Smooch().init('blap')
        print res

if __name__ == '__main__':
    unittest2.main()
