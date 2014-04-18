import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ----------
# General
# ----------
SECRET_KEY = 'for-the-love-of-secrecy-please-change-this-key!'


# ----------
# SQLAlchemy (http://pythonhosted.org/Flask-SQLAlchemy/config.html)
# ----------
DB_USER = 'flask_sandbox'
DB_PASSWORD = 'flask_sandbox'
DB_DATABASE = 'flask_sandbox'
DB_HOST = 'localhost'
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, 
	DB_HOST, DB_DATABASE)
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
SQLALCHEMY_ECHO = True


# ----------
# WTForms (http://wtforms.readthedocs.org/en/latest/)
# ----------
CSRF_ENABLED = True