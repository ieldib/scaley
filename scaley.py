#app.py
import os
from flask import Flask
scaley = Flask(__name__)

@app.route('/')
@app.roue('/home')
def home():
    #add code to check if installed, if not forward to /install
    return render_template('home.html')

@app.route('/install')
def install():
    #add code to check and see if already installed and pass if cond met
    return render_template('install.html')

@app.route('/config')
def config():
    #add code to allow editing of configuration
    return render_template('config.html')


@app.route('/stats')
def stats():
    #add code to give statistical/analytic analysis
    return render_template('stats.html')

@app.route('/migrate')
def migrate():
    #add code to allow some migration tasks from AWS to other cloud providers
    return render_template('migrate.html')


if __name__ == '__main__':
    scaley.run()
