#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from logging import Formatter
from logging.handlers import DatagramHandler


simple_format = \
        '[%(asctime)s][%(levelname)s][%(module)s]: %(message)s'


debug_format = \
        '[%(asctime)s][%(levelname)s][%(module)s][%(pathname)s:' + \
        '%(lineno)d]: %(message)s'


app_name = os.environ.get("app_name", "my_app")


class UDPFormatter(Formatter):

    _format = None

    def __init__(self, fmt=None, datefmt=None, style='%'):
        if fmt is not None:
            super(UDPFormatter, self).__init__(
                    fmt, datefmt, style)
        else:
            super(UDPFormatter, self).__init__(
                    self._format, datefmt, style)

    def format(self, record):
        record.msg = "app_name: " + app_name + ", msg: " + record.msg
        return super(UDPFormatter, self).format(record)


class SimpleFormatter(UDPFormatter):

    _format = simple_format


class DebugFormatter(UDPFormatter):

    _format = debug_format


class UDPHandler(DatagramHandler):

    def __init__(self):
        host = os.environ.get("udp_host", "192.168.5.119")
        port = os.environ.get("udp_port", 29999)
        super(UDPHandler, self).__init__(
                host, port)

    def makePickle(self, record):
        message = self.format(record)
        return message.encode('utf-8')
