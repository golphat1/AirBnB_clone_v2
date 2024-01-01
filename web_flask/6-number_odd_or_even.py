#!/usr/bin/python3
"""
Returning a html script if n is a number
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text_display(text):
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)


@app.route('/python', strict_slashes=False)
def python_without_text():
    return 'Python is cool'


@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    formatted_text_two = text.replace('_', ' ')
    return 'Python {}'.format(formatted_text_two)


@app.route('/number/<int:n>', strict_slashes=False)
def text_is_a_number(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    if (n % 2 == 0):
        return render_template(
            '6-number_odd_or_even.html', number=n, nature='even')
    else:
        return render_template(
            '6-number_odd_or_even.html', number=n, nature='odd')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
