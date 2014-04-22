from flask import Flask, render_template
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Handle HTTP errors
@app.errorhandler(404)
def e_404(error):
	return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable
from app.mod_auth.controllers import mod_auth as auth_mod

# Register blueprints
app.register_blueprint(auth_mod)

from app import views, models