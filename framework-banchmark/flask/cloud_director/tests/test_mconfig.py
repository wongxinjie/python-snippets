# -*- coding: utf-8 -*-
"""
    test_api_v1.py
    ~~~~~~~
    * Copyright (C) 2016 GridSafe, Inc.
"""
import pytest
from app.storage.documents import mongo
from app.storage.documents.room import ModeConfig


@pytest.mark.usefixtures('testapp')
def test_add_config(testapp):
    kwargs = {
        "director_id": 1234,
        "config_name": u"自定义模式",
        "configs": [{}, {}]
    }
    ModeConfig.update("abce", **kwargs)

    kwargs = {
        "director_id": 4567,
        "config_name": u"堆叠",
        "configs": [{}]
    }
    ModeConfig.update("befg", **kwargs)
    assert mongo.db.mconfig.count() == 2


@pytest.mark.usefixtures('testapp')
def test_search_config(testapp):
    kwargs = {
        "configID": "king",
        "director_id": 2456,
        "config_name": u"对话模式",
        "configs": [],
    }
    mongo.db.mconfig.save(kwargs)

    kwargs = {
        "configID": "knig",
        "director_id": 2456,
        "config_name": u"画中画13",
        "configs": [],
    }
    mongo.db.mconfig.save(kwargs)

    kwargs = {
        "configID": "ingk",
        "director_id": 2456,
        "config_name": u"画中画12",
        "configs": [],
    }
    mongo.db.mconfig.save(kwargs)

    rvs = ModeConfig.search(2456)
    assert len(rvs) == 3

    rvs = ModeConfig.search(2456, u"画中画12")
    assert len(rvs) == 1
    assert rvs[0]["configID"] == "ingk"

    rvs = ModeConfig.search(2456, u"画中画", True)
    assert len(rvs) == 2


@pytest.mark.usefixtures('testapp')
def test_delete_channel(testapp):
    kwargs = {
        "configID": "wait",
        "director_id": 1234,
        "config_name": u"会议1",
        "configs": []
    }
    mongo.db.mconfig.save(kwargs)

    kwargs = {
        "configID": "aitw",
        "director_id": 1234,
        "config_name": u"会议1",
        "configs": []
    }
    mongo.db.mconfig.save(kwargs)
    assert mongo.db.mconfig.count() == 2

    ModeConfig.delete("wait")
    assert mongo.db.mconfig.count() == 1
