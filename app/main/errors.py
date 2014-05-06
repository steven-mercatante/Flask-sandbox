from flask import render_template

from . import main

# Handle HTTP errors
@main.app_errorhandler(404)
def e_403(error):
	return render_template('403.html'), 403

@main.app_errorhandler(404)
def e_404(error):
	return render_template('404.html'), 404

@main.app_errorhandler(404)
def e_500(error):
	return render_template('500.html'), 500
