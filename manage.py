import os

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
    	if line.startswith('#'):
    		continue
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]

from app import create_app, db
# Import any models that alembic should be aware of for migrations
from app.auth.models import User

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
	return dict(app=app, db=db, User=User)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def devserver(host='0.0.0.0', port=5000):
	"""Runs a Flask development server.
	Usage: devserver -h 127.0.0.1 -p 5050 to change host and/or port
	"""
	port = int(port)
	app.run(host=host, port=port)

if __name__ == '__main__':
	manager.run()
