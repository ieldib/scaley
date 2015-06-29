#app.py
import os
from flask import Flask
scaley = Flask(__name__)

@app.route('/')
@app.roue('/home')
def home():
    return 'Welcome to Scaley !'

@app.route('/install')
def install():
    open('config.cfg', 'w+')

@app.route('/config')
def config():
    #.... config stuff
    #aws credentials e.t.c.
    pass

@app.route('/stats')
def stats():
    # stats stuff
    # display cloudwatch metrics
    #display openstack metrics e.t.c.
    pass

@app.route('/migrate')
def migrate():
    # migrate stuff here
    pass

if __name__ == '__main__':
    scaley.run()
