import time
import logging
from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(self, request, context):
        start = time.time()
        method_name = func.__name__
        logging.info("%s request: %s", method_name, str(request))
        result = func(self, request, context)
        interval = (time.time() - start) * 1000
        logging.info("%s response: <code=%s, msg=%s>  %.2f ms" % (
            method_name, result.code, result.msg, interval
        ))
        return result

    return wrapper
