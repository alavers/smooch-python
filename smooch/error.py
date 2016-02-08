class SmoochError(Exception):

    def __init__(self, message=None, res=None):
        super(SmoochError, self).__init__(message)
        if (res):
            self.status_code = res.status_code
