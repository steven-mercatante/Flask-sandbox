from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()

# app = Flask(__name__)
# app.config.from_object('config')



# Import a module / component using its blueprint handler variable
# from app.mod_auth.views import mod_auth as auth_mod

# Register blueprints

# app.register_blueprint(auth_mod)

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)

	db.init_app(app)

	login_manager = LoginManager()
	login_manager.init_app(app)
	login_manager.login_view = 'auth.login'
	
	# Register Blueprints
	from main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	return app
# from app import views, models