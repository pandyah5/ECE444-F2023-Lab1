from flask import Flask, render_template
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from datetime import datetime

app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, currentTime=datetime.utcnow())
