Tips
----
- Read configuration settings when in a view with the `{{ config }}` dict
- Jinja2 global variables: http://flask.pocoo.org/docs/templating/#standard-context
- Fetch the current app: `from flask import current_app as app`
- Check if a user is logged in: `current_user.is_authenticated()`