#app.py
import os
from flask import Flask
scaley = Flask(__name__)

@app.route('/')
@app.roue('/home')
def home():
    return render_template('home.html')

@app.route('/install')
def install():
    #add code to check and see if already installed and pass if cond met
    return render_template('install.html')

@app.route('/config')
def config():
    return render_template('hello.html')


@app.route('/stats')
def stats():
    return render_template('stats.html')

@app.route('/migrate')
def migrate():
    return render_template('migrate.html')


if __name__ == '__main__':
    scaley.run()
