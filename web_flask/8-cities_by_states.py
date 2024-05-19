#!/usr/bin/python3
"""web app"""

from models import *
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states')
def state_list():
    """alphabetic order of states and cities"""
    st = storage.all("State").values()
    return render_template('8-cities_by_states.html', st=st)


@app.teardown_appcontext
def app_teardown(arg=None):
    """closes storage"""
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port='5000')
