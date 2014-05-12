from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	bootstrap.init_app(app)
	mail.init_app(app)
	moment.init_app(app)
	db.init_app(app)
	login_manager.init_app(app)

	# Register Blueprints
	# TODO: reduce boilerplate by listing blueprints in a dict and iterating
	# over them to register them
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	from .sandbox import sandbox as sandbox_blueprint
	app.register_blueprint(sandbox_blueprint)

	return app
