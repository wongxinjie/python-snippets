# coding: utf-8
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, **args):
        for field, value in args.items():
            self.__setattr__(field, value)

    def update(self):
        db.session.commit()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def model2dict(self):
        rvs = {}
        for key, val in self.__dict__.items():
            if key.startswith('_') or key.startswith('__'):
                continue
            if isinstance(val, datetime):
                val = val.strftime('%Y-%m-%d %H:%M:%S')
            rvs[key] = val
        return rvs
