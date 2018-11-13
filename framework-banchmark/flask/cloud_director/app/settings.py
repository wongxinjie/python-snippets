# coding: utf-8
import os


class Config(object):
    # sentry client key

    SECRET_KEY = '1zrEhCo0brf1vVlqmP7eqn6pTQFA2MBhvEzt0l7dU+Q'
    DEBUG = int(os.environ.get('DEBUG', 0)) == 1

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI',
        'mysql+pymysql://root:@localhost:3306/flask_banchmark'
    )
    REDIS_URL = os.environ.get(
        'REDIS_URL', 'redis://:@localhost:6379/0')

    # logging设置
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,

        'formatters': {
            'simple': {
                'format': '%(asctime)s %(levelname)s# %(message)s'
            }
        },

        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple',
                },
            },

        'loggers': {
            '': {
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False,
                },
        }
    }

    @classmethod
    def init_app(self, app):
        pass
