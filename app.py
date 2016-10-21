from flask import Flask, render_template
from config import Configuration
from datetime import datetime

from flask_bootstrap import Bootstrap  # Make Bootstrap support 

from flask_moment import Moment # Make Moment support 

app = Flask(__name__)

app.config.from_object(Configuration)  # read configuration from config

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def paget_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()