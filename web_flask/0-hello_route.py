#!/usr/bin/python3
"""Simple Flask project"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def diplay():
	"""Display Hello message"""
	return 'Hello HBNB!'


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
