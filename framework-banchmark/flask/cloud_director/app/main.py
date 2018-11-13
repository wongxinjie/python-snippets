# coding: utf-8
from flask import Flask

from app.settings import Config
from app.models import db

from app.views.demo import demo


def create_app():
    app = Flask(__name__)
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', True)
    app.config.from_object(Config)
    Config.init_app(app)

    db.init_app(app)
    # add other flask extensions

    app.register_blueprint(demo, url_prefix='')
    # add blueprint here
    return app
