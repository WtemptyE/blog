from flask import Flask, render_template
from config import Configuration

from flask_bootstrap import Bootstrap  # Make Bootstrap support 

app = Flask(__name__)

app.config.from_object(Configuration)  # read configuration from config

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run()