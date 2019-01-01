from gevent import monkey
from gevent.pywsgi import WSGIServer

from flaskapp import app

monkey.patch_all()

server = WSGIServer(("127.0.0.1", 8080), app)
server.serve_forever()
