from flask import jsonify
from . import api


class GenericException(Exception):
    """
    Generic Custom Exception. Inherit from Exception.

    :type message: string
    :param message: Message to show in the exception.

    :type status_code: int
    :param status_code: HTTP Status Code.

    :type payload: dict
    :param payload: Aditional information.
    """
    def __init__(self, message=None, status_code=None, payload=None):
        super(GenericException, self).__init__()
        if message is not None:
            self.message = message

        if status_code is not None:
            self.status_code = status_code

        self.payload = payload
        self.headers = None
        if self.payload is not None and self.payload['headers'] is not None and self.payload['headers'] != '':
            self.headers = self.payload['headers']

    def to_dict(self):
        """
        Convert a message to dictionary.
        """
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

class InternalServerErrorException(GenericException):
    """
    Internal Server Error Exception. Inherit from GenericException.

    :type message: string
    :param message: Message to show in the exception.

    :type status_code: int
    :param status_code: HTTP Status Code.

    :type payload: dict
    :param payload: Aditional information.
    """
    status_code = 500
    message = 'An internal server error has ocurred'

    def __init__(self, message=None, status_code=None, payload=None):
        super(InternalServerErrorException, self).__init__(message, status_code, payload)

def handle_exceptions(error):
    """
    Handle exception error response.

    :type error: string
    :param error: Error message.

    :rtype: object
    :return: Response Object.
    """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    if not error.headers is None:
        response.headers = error.headers
    return response

@api.errorhandler(InternalServerErrorException)
def handle_internal_server_error(error):
    """
    Handle Internal Server error.

    :type error: string
    :param error: Error message.
    """
    return handle_exceptions(error)

class BadRequestException(GenericException):
    """
    Bad Request Exception. Inherit from GenericException.

    :type message: string
    :param message: Message to show in the exception.

    :type status_code: int
    :param status_code: HTTP Status Code.

    :type payload: dict
    :param payload: Aditional information.
    """
    status_code = 400
    message = 'Bad Request'

    def __init__(self, message=None, status_code=None, payload=None):
        super(BadRequestException, self).__init__(message, status_code, payload)


@api.errorhandler(BadRequestException)
def handle_bad_request(error):
    """
    Handle bad request error.

    :type error: string
    :param error: Error message.
    """
    return handle_exceptions(error)

class NotFoundException(GenericException):
    """
    Not Found Exception. Inherit from GenericException.

    :type message: string
    :param message: Message to show in the exception.

    :type status_code: int
    :param status_code: HTTP Status Code.

    :type payload: dict
    :param payload: Aditional information.
    """
    status_code = 404
    message = '404 Not Found'

    def __init__(self, message=None, status_code=None, payload=None):
        super(NotFoundException, self).__init__(message, status_code, payload)

@api.app_errorhandler(404)
def page_not_found(error):
    """
    Error handler for 'not found' errors.

    :type error: string
    :param error: Error message.
    """
    response = jsonify({'error': 'Not Found'})
    response.status_code = 404
    return response

class ForbiddenException(GenericException):
    """
    Forbidden Exception. Inherit from GenericException.

    :type message: string
    :param message: Message to show in the exception.

    :type status_code: int
    :param status_code: HTTP Status Code.

    :type payload: dict
    :param payload: Aditional information.
    """
    status_code = 403
    message = 'Forbidden'

    def __init__(self, message=None, status_code=None, payload=None):
        super(ForbiddenException, self).__init__(message, status_code, payload)

@api.errorhandler(ForbiddenException)
def handle_bad_request(error):
    """
    Handle bad request error.

    :type error: string
    :param error: Error message.
    """
    return handle_exceptions(error)

class NotAuthorizedException(GenericException):
    """
    Now Authorized Exception. Inherit from GenericException.

    :type message: string
    :param message: Message to show in the exception.

    :type status_code: int
    :param status_code: HTTP Status Code.

    :type payload: dict
    :param payload: Aditional information.
    """
    status_code = 401
    message = '401 Not Authorized'

    def __init__(self, message=None, status_code=None, payload=None):
        super(NotAuthorizedException, self).__init__(message, status_code, payload)

@api.errorhandler(NotAuthorizedException)
def handle_not_authorized(error):
    """
    Handle not authorized error.

    :type error: string
    :param error: Error message.
    """
    return handle_exceptions(error)
