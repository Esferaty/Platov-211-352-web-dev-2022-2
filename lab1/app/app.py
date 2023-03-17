from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, world!'

    # set FLASK_APP=app.py

    # export FLASK_APP=app.py