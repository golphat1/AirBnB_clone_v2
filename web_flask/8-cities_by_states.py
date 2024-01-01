#!/usr/bin/python3
"""
A script showing cities by states
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all("State")
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    storage.reload()
    app.run(host='0.0.0.0', port=5000)
