import re
import json
from collections import MutableMapping

snake_case = re.compile('(?<!^)_([a-z0-9])')


class SmoochResource(MutableMapping):

    def __init__(self, *args, **kwargs):
        all_args = kwargs

        if len(args) > 0 and type(args[0]) == dict:
            all_args.update(args[0])

        all_args = dict(
            map(lambda (k, v): (self._key_transform(k), v),
                all_args.iteritems()))

        # validate optional and required args
        optional_attrs = self._optional_attrs()
        required_attrs = self._required_attrs()
        all_attrs = optional_attrs.union(required_attrs)
        unknown_args = set(all_args.keys()).difference(all_attrs)
        if unknown_args:
            raise ValueError("'%s' recieved invalid argument(s): '%s'" %
                             (type(self).__name__, ', '.join(unknown_args)))

        missing_args = required_attrs.difference(set(all_args.keys()))
        if missing_args:
            raise ValueError("'%s' missing argument(s): '%s'" %
                             (type(self).__name__, ', '.join(missing_args)))

        self._store = dict()
        self.update(all_args)

    def __setattr__(self, key, value):
        if key[0] == '_' or key in self.__dict__:
            return super(SmoochResource, self).__setattr__(key, value)
        else:
            self._store[self._key_transform(key)] = value

    def __getattr__(self, key):
        if key[0] == '_':
            raise AttributeError(key)

        try:
            return self._store[self._key_transform(key)]
        except KeyError:
            raise AttributeError("'%s' object has no attribute '%s'" %
                                 (type(self).__name__, key))

    def __delattr__(self, key):
        del self._store[key]

    def __getitem__(self, key):
        return self._store[self._key_transform(key)]

    def __setitem__(self, key, value):
        self._store[self._key_transform(key)] = value

    def __delitem__(self, key):
        del self._store[self._key_transform(key)]

    def __iter__(self):
        return iter(self._store)

    def __len__(self):
        return len(self._store)

    def _key_transform(self, key):
        # camelize keys, eg given_name --> givenName
        return re.sub(snake_case, lambda pat: pat.group(1).upper(), key)

    @classmethod
    def _optional_attrs(cls):
        return set()

    @classmethod
    def _required_attrs(cls):
        return set()

    def json(self):
        return json.dumps(self._store)


class AppUser(SmoochResource):

    @classmethod
    def _optional_attrs(cls):
        return {
            '_id', 'givenName', 'surname', 'email', 'signedUpAt',
            'conversationStarted', 'properties'}


class Device(SmoochResource):

    def __init__(self, *args, **kwargs):
        super(Device, self).__init__(*args, **kwargs)
        if not hasattr(self, 'platform'):
            self.platform = 'other'

    @classmethod
    def _required_attrs(cls):
        return {'id'}

    @classmethod
    def _optional_attrs(cls):
        return {'platform'}
