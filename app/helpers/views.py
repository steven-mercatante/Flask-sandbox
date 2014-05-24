from flask import current_app, g

def set_page_title(title=None, prefix=None, suffix=None, separator='-', separate_with_spaces=True):
	if not title:
		title = current_app.config['TITLE']
	if separate_with_spaces:
		separator = ' ' + separator + ' '
	if prefix:
		title = '{prefix}{separator}{title}'.format(prefix=prefix, separator=separator, title=title)
	if suffix:
		title = '{title}{separator}{suffix}'.format(title=title, separator=separator, suffix=suffix)
	g.title = title
	return g.title

def get_page_title():
	if g.get('title'):
		return g.title
	return current_app.config['TITLE']
