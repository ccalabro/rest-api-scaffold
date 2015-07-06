"""Module v0.0.1 API"""
from flask import Blueprint

api = Blueprint('api', __name__)

from views import root
