# coding: utf-8
import pytest

from app.main import create_app
from app.storage.models import db
from app.storage.documents import mongo


@pytest.fixture()
def testapp(request):
    app = create_app('testing')
    client = app.test_client()
    app_context = app.app_context()
    app_context.push()

    db.create_all()

    def setup():
        mongo.db.directors.remove()
        mongo.db.mconfig.remove()

    def teardown():
        db.session.remove()
        mongo.db.directors.remove()
        mongo.db.mconfig.remove()
        db.drop_all()
        app_context.pop()

    request.addfinalizer(teardown)
    return client
