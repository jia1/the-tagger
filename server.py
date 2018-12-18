from os import environ
from gevent.pywsgi import WSGIServer
from app import app

if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()

