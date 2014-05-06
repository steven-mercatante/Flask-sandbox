from flask import render_template, flash, redirect, session, url_for, request, g

from . import main
from .. import db

@main.route('/')
def index():
	return render_template('main/index.html')