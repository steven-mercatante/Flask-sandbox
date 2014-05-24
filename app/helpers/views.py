from flask import current_app

def page_title():
	return current_app.config['TITLE']