class NotAuthorizedException(Exception):
    pass


class UnsupportedMethodException(Exception):
    pass


class WrongResponseException(Exception):
    pass


class EmptyResponse(KeyError):
    pass
