# -*- coding: utf-8 -*-

"""
    backend_tasks.py
    ~~~~~~~
    用于后台停止已经销毁的导播台等

    * Copyright (C) 2016 GridSafe, Inc.
"""
import time
import logging

from app.main import create_app
from app.backends import clean_disable_directors

SERVER_STATUS_CRONTAB_TIME = 30

_app = create_app("prod")


def run_crontab():
    while True:
        with _app.app_context():
            clean_disable_directors()
        time.sleep(SERVER_STATUS_CRONTAB_TIME)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(levelname)s# %(message)s",
                        datefmt="%Y/%m/%d-%H:%M:%S")
    run_crontab()
