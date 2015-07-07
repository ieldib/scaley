from os import environ
from scaley import app
from scaley.module import db


if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 5555
    app.config['DEBUG'] = True  #need to move these config lines to modules.config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db/scaley.db'
    app.run(HOST, PORT)
