from flask import render_template, flash, redirect, session, url_for, request, g

from app import app


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')