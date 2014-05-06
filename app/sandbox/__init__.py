from flask import Blueprint

sandbox = Blueprint('sandbox', __name__, url_prefix='/sandbox')

from . import views