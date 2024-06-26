#!/usr/bin/python3
"""Simple Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display the text 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def say_hbnb():
    """Display the text 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Display 'C' followed by the text variable."""
    t = text.replace("_", " ")
    return "C {}".format(t)

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route that displays 'Python ' followed by the value of the text variable."""
    t = text.replace("_", " ")
    return "Python {}".format(t)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
