Initial Python setup:
---------------------
- Populate `.env` with real values
- Setup virtual environment in project root dir: `virtualenv venv`
- Activate the virtual environment: `source venv/bin/activate`
- Install Python dependencies: `pip install -r requirements.txt`

Initial database setup:
-----------------------
- Create the migrations directory: `python manage.py db init`
- Create the intial DB migration: `python manage.py db migrate`
- Run DB migrations: `python manage.py db upgrade`

Connect to Vagrant database from host machine:
----------------------------------------------
- MySQL Host: `127.0.0.1`
- Username: `see configuration setting`
- Password: `see configuration setting`
- Port: `3306`
- SSH Host: `127.0.0.1`
- SSH User: `vagrant`
- SSH Key: `~/.vagrant.d/insecure_private_key`
- SSH Port: `2220`

Common tasks:
-------------
- Start a local development server: `python manage.py devserver`

Working within Vagrant:
-----------------------
- Login: `vagrant ssh`
- Change directory to project root: `cd /vagrant`
- Activate the virtual environment: `source venv/bin/activate`
Note: the plan is to have the above steps performed automatically upon SSHing into the Vagrant box.

Vagrant notes:
--------------
- `Vagrantfile` lists the forwarded ports. They're commonly `80 -> 8080`, `5000 -> 5050`, `22 -> 2220`
- Development server should be run on `0.0.0.0` so that it can be accessed from your host machine. 

Working with models:
--------------------
- Model classes should extend the `Base` model (`app/models.py`). See `app/auth/models.py` for an example.
- Defining a `__repr__` method is highly recommended for debugging purposes.
- To enable migration support, import the model within `manage.py`. Ex: `from app.main.models import Person`. Usage of `from app.main.models import *` is discouraged as per "[explicit is better than implicit](http://legacy.python.org/dev/peps/pep-0020/)"
- *IMPORTANT: Alembic does a good job building DB migrations, but it isn't perfect. You may see errors in the console when building migrations - don't panic! Just spot check the migration and fix any errors, then run `python manage.py db upgrade`.*

Tips:
-----
- Jump into a project specific Python shell: `python manage.py shell`
- To work with models within a project shell, you must first add a reference to it in `manage.py`'s `make_shell_context` method.
