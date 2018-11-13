import time
import logging
from functools import partial
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor

import tornado
from tornado import web
from tornado import gen
from tornado import ioloop
from tornado import httpserver
from tornado import httpclient
from tornado.options import options, define, parse_command_line
from tornado.concurrent import run_on_executor

from celery_tasks import fetch_content

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s# %(message)s",
    datefmt="%Y/%m/%d-%H:%M:%S"
)
define("port", default=9090, type=int)


class BaseHandler(web.RequestHandler):

    def initialize(self):
        self.start = time.time()

    def get_block_seconds(self):
        t = self.get_argument("t", 5)
        t = int(t) if t.isdigit() else 5
        return t

    def on_finish(self):
        end = time.time()
        logging.info("{}-runtime: {}s".format(
            self.__class__.__name__, end - self.start))


class ExecutorHandler(BaseHandler):
    executor = ThreadPoolExecutor()

    @gen.coroutine
    def get(self):
        url = self.get_argument("url", "https://httpbin.org/")
        response = yield self.fetch(url)
        self.write("pageSize is %s" % len(response))
        self.finish()

    @run_on_executor
    def fetch(self, url):
        with urlopen(url) as page:
            content = page.read().decode("utf-8")
        return content


class BlockHandler(BaseHandler):
    @web.asynchronous
    def get(self):
        seconds = self.get_block_seconds()
        time.sleep(seconds)
        self.write('I sleep for %s' % seconds)
        self.finish()


class CoroutineHandler(BaseHandler):

    @web.asynchronous
    @gen.coroutine
    def get(self):
        yield gen.Task(ioloop.IOLoop.instance().add_timeout, time.time() + 10)
        self.write("I sleep for 10s")


class CallbackHandler(BaseHandler):

    @web.asynchronous
    def get(self):
        ioloop.IOLoop.instance().add_timeout(
            time.time() + 5, callback=self.on_response)

    def on_response(self):
        self.write("I sleep for 10s")
        self.finish()


class CallbackFetchHandler(BaseHandler):

    @web.asynchronous
    def get(self):
        url = self.get_argument("url", "https://httpbin.org/")
        client = httpclient.AsyncHTTPClient()
        client.fetch(url, self._on_response)

    def _on_response(self, response):
        size = len(response.body)
        self.write("pageSize is %s" % size)
        self.finish()


class GenAsyncHandler(BaseHandler):

    @gen.coroutine
    def get(self):
        url = self.get_argument("url", "https://httpbin.org/")
        client = httpclient.AsyncHTTPClient()
        response = yield client.fetch(url)
        self.write("pageSize is %s" % len(response.body))


class NormalHandler(BaseHandler):

    def get(self):
        self.write('Time: {}'.format(time.time()))


class CeleryAsyncHandler(BaseHandler):

    def wait_for_result(self, task, callback):
        if task.ready():
            callback(task.result)
        else:
            tornado.ioloop.IOLoop.current().add_callback(
                partial(self.wait_for_result, task, callback)
            )

    @gen.coroutine
    def get(self):
        url = self.get_argument("url", "https://httpbin.org/")
        task = fetch_content.apply_async(args=(url, ))
        content = yield gen.Task(self.wait_for_result, task)
        self.write("pageSize is %s" % len(content))


class runserver():
    parse_command_line

    app = web.Application(
        handlers=[
            (r'/executor', ExecutorHandler),
            (r'/block', BlockHandler),
            (r'/time', NormalHandler),
            (r'/callback-fetch', CallbackFetchHandler),
            (r'/gen-fetch', GenAsyncHandler),
            (r'/coroutine', CoroutineHandler),
            (r'/callback', CallbackHandler),
            (r'/celery', CeleryAsyncHandler),
        ]
    )

    http_server = httpserver.HTTPServer(app)
    http_server.listen(options.port)
    ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    runserver()
