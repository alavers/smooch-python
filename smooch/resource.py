class AppUser(object):

    def __init__(self, json):
        self._id = json['_id']
        self.signed_up_at = json['signedUpAt']
        self.conversation_started = json['conversationStarted']
        self.properties = json['properties']


class Device(object):

    def __init__(self, id, platform='other'):
        self.id = id
        self.platform = platform
