from flask import abort, render_template, flash, redirect, session, url_for, \
	request, g	

from .. import db
from . import main

@main.route('/')
def index():
	return render_template('main/index.html')