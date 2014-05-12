from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/auth')

from . import views, models
from .. import login_manager

login_manager.anonymous_user = models.AnonymousUser

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))