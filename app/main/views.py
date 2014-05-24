from flask import abort, render_template, flash, redirect, session, url_for, \
	request, g	

from .. import db
from .. helpers.views import set_page_title
from . import main

@main.route('/')
def index():
	set_page_title(title='New title', prefix='PRE',suffix='POST')
	return render_template('main/index.html')