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

Common tasks:
-------------
- Start a local development server: `python manage.py devserver`

Working within Vagrant:
-----------------------
- Login: `vagrant ssh`
- Change directory to project root: `cd /vagrant`
- Activate the virtual environment: `source venv/bin/activate`

Vagrant notes:
--------------
- `Vagrantfile` lists the forwarded ports. They're commonly `80 -> 8080`, `5000 -> 5050`, `22 -> 2220`
 
