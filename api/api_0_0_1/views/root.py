from flask import jsonify
from .. import api
from ..exceptions import *


@api.route('/')
def index():
    """Index method."""
    try:
        message = {
            'message': 'Welcome to Example REST API.'
        }

        response = jsonify(message)
        response.status_code = 200

        return response
    except:
        raise InternalServerErrorException()
