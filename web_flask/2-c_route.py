#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_root():
	"""Hello HBNB!"""
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
	"""HBNB"""
	return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
	""" C  followed by the value of the text"""
	t = text.remplace("_", " ")
	return "C {}".format(t)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
