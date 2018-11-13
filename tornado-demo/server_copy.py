import tornado.ioloop
import tornado.web
from tornado.log import access_log


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        access_log.error("Me")
        self.write("hello, world")

    def on_finish(self):
        print(self.request.request_time())


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
