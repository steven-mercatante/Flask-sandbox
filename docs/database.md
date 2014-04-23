## Migrations ##
- Flask-Alembic(https://github.com/miguelgrinberg/Flask-Migrate) on top of Alembic (https://pypi.python.org/pypi/alembic/) is used
  to manage database migrations.
- Alembic does a lot of work for us, but it can't do everything. Before upgrading or downgrading the database, manually check the
  migration file to make sure all the alterations are correct. Additionally, indexes will need to be added or dropped manually. In some
  cases it's possible to hand write these index operations in the migration file.

## Getting Started With Alembic ##
- `manage.py db init`
- `manage.py db migrate`
- `manage.py db upgrade` (or `downgrade`)