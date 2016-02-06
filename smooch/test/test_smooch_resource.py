from unittest2 import TestCase, main
from smooch.resource import SmoochResource, AppUser, Device


class Foo(SmoochResource):

    @classmethod
    def _required_attrs(cls):
        return set(['fooBar'])

    @classmethod
    def _optional_attrs(cls):
        return set(['baz', 'qux'])


class SmoochResourceTests(TestCase):

    def test_constructor(self):
        foo = Foo(foo_bar='Steve')
        self.assertIsInstance(foo, Foo)

    def test_optional_attrs(self):
        foo = Foo(foo_bar='Steve', qux='Brule')
        self.assertEqual(foo.foo_bar, 'Steve')
        self.assertEqual(foo.qux, 'Brule')
        self.assertNotIn('baz', foo.keys())

    def test_camel_case(self):
        foo = Foo(fooBar='Steve')
        self.assertEquals(foo.foo_bar, 'Steve')
        self.assertEquals(foo.fooBar, 'Steve')

    def test_snake_case(self):
        foo = Foo(foo_bar='Steve')
        self.assertEquals(foo.foo_bar, 'Steve')
        self.assertEquals(foo.fooBar, 'Steve')

    def test_from_dict(self):
        foo = Foo({'fooBar': 'Steve'})
        self.assertEquals(foo.fooBar, 'Steve')

    def test_invalid_params(self):
        with self.assertRaisesRegexp(ValueError, "recieved invalid argument"):
            Foo(invalid='invalid')


class AppUserTests(TestCase):

    def test_from_attrs(self):
        app_user = AppUser(given_name='Steve')
        self.assertEquals(app_user.givenName, 'Steve')

    def test_from_dict(self):
        app_user = AppUser({'givenName': 'Steve'})
        self.assertEquals(app_user.givenName, 'Steve')


class DeviceTests(TestCase):

    def test_from_attrs(self):
        device = Device(id='banana')
        self.assertEquals(device.id, 'banana')

    def test_from_dict(self):
        device = Device({'id': 'banana'})
        self.assertEquals(device.id, 'banana')

if __name__ == '__main__':
    main()
