import os

from paste.deploy import loadapp
from wsgiref.simple_server import make_server

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app = loadapp('config:production.ini', relative_to='.')
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
