#!/usr/bin/python3
"""my first module"""


from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """hello world from the root"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbhb():
    """hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text=""):
    """hbnb"""
    text = text.replace('_', ' ')
    return ('C ' + text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """hbnb"""
    text = text.replace('_', ' ')
    return ('Python ' + text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """hbnb"""
    return (str(n) + ' is a number')


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """hbnb"""
    return (render_template('5-number.html', n=n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # debug=True, which will be beneficial if you plan to make changes
    # and want the server to automatically reload
    # and provide helpful debugging information.
