from os import environ
from scaley import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8080'))
    except ValueError:
        PORT = 5555
    app.config['DEBUG'] = True
    app.run(HOST, PORT)
