import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'placeholder secret'

	CSRF_ENABLED = True

	DB_USER = 'flask_sandbox'
	DB_PASSWORD = 'flask_sandbox'
	DB_DATABASE = 'flask_sandbox'
	DB_HOST = 'localhost'
	SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, 
		DB_HOST, DB_DATABASE)
	SQLALCHEMY_ECHO = True
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	@staticmethod
	def init_app(app):
		pass


class DevConfig(Config):
	DEBUG = True


class TestingConfig(Config):
	TESTING = True
	WTF_CSRF_ENABLED = False


class ProdConfig(Config):
	SQLALCHEMY_ECHO = False


config = {
	'dev': DevConfig,
	'testing': TestingConfig,
	'prod': ProdConfig,
	'default': DevConfig
}
