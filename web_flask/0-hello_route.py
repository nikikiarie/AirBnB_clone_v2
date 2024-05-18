#!/usr/bin/python3
"""Start flask appplication"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def flask_hello():
    """Returns Hello HBNB string"""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
