#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def handle_close(self):
    """
    Request you must remove the current
    SQLAlchemy Session.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def handle_states():
    all_states = storage.all(State).values()
    sort_states = sorted(all_states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sort_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
