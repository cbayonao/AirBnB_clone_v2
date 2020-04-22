#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask
from flask import render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """
    Function to print hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
    Function to print HBNB!
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """
    C is fun!
    """
    return 'C %s' % text.replace('_', ' ')


@app.route("/python")
@app.route('/python/<text>/')
def py_text(text='is cool'):
    """Python is Cool"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def only_int(n):
    """Is it a number?"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def num_template(n):
    """Number template"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """Odd or even?"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
