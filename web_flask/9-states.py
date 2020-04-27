#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from os import environ
app = Flask(__name__)


@app.teardown_appcontext
def handle_close(self):
    """
    Request you must remove the current
    SQLAlchemy Session.
    """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def handle_states_state(id=""):
    """
    States and State
    """
    all_states = storage.all(State).values()
    sort_states = sorted(all_states, key=lambda state: state.name)
    found = 0
    state = ""
    cities = []

    for i in sort_states:
        if id == i.id:
            state = i
            found = 1
            break
    if found:
        sort_states = sorted(state.cities, key=lambda state: state.name)
        state = state.name

    if id and not found:
        found = 2

    return render_template('9-states.html',
                           state=state,
                           array=sort_states,
                           found=found)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
