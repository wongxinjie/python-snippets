# -*- coding: utf-8 -*-
"""
    test_api_v1.py
    ~~~~~~~
    * Copyright (C) 2016 GridSafe, Inc.
"""
import pytest
from app.storage.documents.room import Channels, mongo


@pytest.mark.usefixtures('testapp')
def test_add_channel(testapp):
    kwargs = {
        "streamID": 1234,
        "1": "http://www.cdnzzlive1.com",
        "2": "http://www.cdnzzlive2.com",
        "3": "http://www.cdnzzlive3.com"
    }
    Channels.insert(**kwargs)

    kwargs = {
        "streamID": 3456,
        "1": "http://www.cdnzzlive4.com",
        "2": "http://www.cdnzzlive5.com",
        "3": "http://www.cdnzzlive6.com"
    }
    Channels.insert(**kwargs)
    assert mongo.db.directors.count() == 2


@pytest.mark.usefixtures('testapp')
def test_update_channel(testapp):
    kwargs = {
        "streamID": 3456,
        "1": "http://www.cdnzzlive4.com",
        "2": "http://www.cdnzzlive5.com",
        "3": "http://www.cdnzzlive6.com"
    }
    mongo.db.directors.save(kwargs)

    Channels.update(3456, **{"1": "http://www.cdnzzlive7.com"})
    rv = mongo.db.directors.find_one({"streamID": 3456})
    assert rv is not None
    assert rv["1"] == "http://www.cdnzzlive7.com"
    assert rv["2"] == "http://www.cdnzzlive5.com"
    assert rv["3"] == "http://www.cdnzzlive6.com"


@pytest.mark.usefixtures('testapp')
def test_search_channel(testapp):
    kwargs = {
        "streamID": 3456,
        "1": "http://www.cdnzzlive4.com",
        "2": "http://www.cdnzzlive5.com",
        "3": "http://www.cdnzzlive6.com"
    }
    mongo.db.directors.save(kwargs)

    rv = Channels.search(3456)
    assert rv is not None
    assert rv["1"] == "http://www.cdnzzlive4.com"
    assert rv["2"] == "http://www.cdnzzlive5.com"
    assert rv["3"] == "http://www.cdnzzlive6.com"

    rv = Channels.search(7890)
    assert rv is None


@pytest.mark.usefixtures('testapp')
def test_delete_channel(testapp):
    kwargs = {
        "streamID": 3456,
        "1": "http://www.cdnzzlive4.com",
        "2": "http://www.cdnzzlive5.com",
        "3": "http://www.cdnzzlive6.com"
    }
    mongo.db.directors.save(kwargs)
    Channels.delete(3456)

    kwargs = {
        "streamID": 1234,
        "1": "http://www.cdnzzlive1.com",
        "2": "http://www.cdnzzlive2.com",
        "3": "http://www.cdnzzlive3.com"
    }
    mongo.db.directors.save(kwargs)

    rv = mongo.db.directors.find_one({"streamID": 3456})
    assert rv is None

    rv = mongo.db.directors.find_one({"streamID": 1234})
    assert rv is not None
