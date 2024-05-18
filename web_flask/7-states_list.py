#!/usr/bin/python3
"""Flask application"""


from models import storage
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list')
def states_lst():
    """html page with states in alphabetic order"""
    list_st = sorted(list(storage.all("State").values()), key=lambda i: i.name)
    return render_template('7-states_list.html', list_st=list_st)


@app.teardown_appcontext
def app_teardown(arg=None):
    """closes storage"""
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
