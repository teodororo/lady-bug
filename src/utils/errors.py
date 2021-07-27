class HTTPError(Exception):

    def __init__(self, message=""):
        self.message = message
        self.status = 400
        self.type = self.__class__.__name__
        self.title = None


class HTTPClientError(HTTPError):

    def __init__(self, errors=None, model="", path=[], **kwargs):
        super().__init__(**kwargs)
        self.model = model
        self.status = 400
        self.errors = errors
        self.path = path
        self.title = "Client Error."