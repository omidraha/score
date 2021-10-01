class ServiceException(Exception):
    """
    Base class for service framework exceptions.
    """
    message = 'An service error occurred, please contact administrator'


class AppException(Exception):
    """
    Base class for App framework exceptions.
    """
    message = 'An application error occurred.'


class EmptyToken(ServiceException):
    message = 'The token is not set correctly'


class InvalidToken(ServiceException):
    message = 'The token is not valid'


class RepoIsNotExist(AppException):
    message = 'The repository does not exist!'
