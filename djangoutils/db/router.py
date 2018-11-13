# -*- coding: utf-8 -*-

"""
* Copyright (C) 2016 GridSafe, Inc.
"""


class DbRouter(object):
    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        if hasattr(model, 'connection_name'):
            return model.connection_name
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        if hasattr(model, 'connection_name'):
            return model.connection_name
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """

        if obj1._state.db != obj2._state.db:
            return None
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return None
