import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'placeholder secret'

	CSRF_ENABLED = True

	TITLE = 'Flask Sandbox'

	DB_HOST = os.environ.get('DB_HOST')
	DB_USER = os.environ.get('DB_USER')
	DB_PASSWORD = os.environ.get('DB_PASSWORD')
	DB_DATABASE = os.environ.get('DB_DATABASE')
	SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}/{}'.format(DB_USER, 
		DB_PASSWORD, DB_HOST, DB_DATABASE)
	SQLALCHEMY_ECHO = True
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True

	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MAIL_PORT = os.environ.get('MAIL_PORT')
	MAIL_SENDER = os.environ.get('MAIL_SENDER')
	MAIL_USE_TLS = True

	ADMIN_EMAILS = [
		'steven.mercatante@gmail.com'
	]

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
