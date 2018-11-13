# coding: utf-8
from datetime import datetime

from app.models import db, Base


class Seqver(Base):

    __tablename__ = "seqver"

    seqver = db.Column(db.Integer, nullable=False)
    uuid = db.Column(db.String(64), nullable=False)

    created_on = db.Column(db.DateTime, default=datetime.now())
