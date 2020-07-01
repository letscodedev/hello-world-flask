# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/
import automate
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return automate()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)
