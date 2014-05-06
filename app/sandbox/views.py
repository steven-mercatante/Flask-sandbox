from flask import render_template

from . import sandbox

@sandbox.route('/')
@sandbox.route('/index')
def index():
	return render_template('sandbox/index.html')