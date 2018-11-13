# -*- coding: utf-8 -*-

from django.apps import apps
from django.core import serializers
from django.db import models
from django.core.cache import caches

import hashlib


class CacheQuery(object):
    """A implement of cache using redis and DjangoORM
    """

    def __init__(self, cache_name='default'):
        self.cache = self.get_cache(cache_name)
        self.expire = 5 * 60

    def get_cache(self, cache_name):
        cache = caches[cache_name]
        return cache

    def get_cache_key(self, model, connection_name, **kwargs):
        if not connection_name:
            if hasattr(model, 'connection_name'):
                connection_name = model.connection_name
            else:
                connection_name = 'default'

        db_table = model._meta.db_table
        query_str = '&'.join(['%s=%s' % (k, v) for k, v in kwargs.items()])
        query_md5 = hashlib.md5(query_str.encode('utf-8')).hexdigest()
        return 'cache::%s::%s::%s' % (connection_name, db_table, query_md5)

    def get_from_cache(self, model, connection_name,
                       cache_name=None, **kwargs):
        if cache_name:
            cache = self.get_cache(cache_name)
        else:
            cache = self.cache

        cache_key = self.get_cache_key(model, connection_name, **kwargs)
        cached_instances = cache.get(cache_key)

        if not cached_instances:
            instances = model.objects.filter(**kwargs)
            if connection_name:
                instances = instances.using(connection_name)

            serialize_instances = serializers.serialize('json', instances)
            cache.set(cache_key, serialize_instances, self.expire)
        else:
            serialize_instances = serializers.deserialize(
                'json', cached_instances)
            instances = [deinstance.object
                         for deinstance in serialize_instances]

        return instances

    def query(self, model, connection_name=None, cache_name='default',
              flat=False, **kwargs):
        """general function for using cache

        :param ModelBase model: The model to be cached
        :param str connection_name: db name in settings.DATABASES
        :param str cache_name: cache db name in settings.CACHES
        :param bool flat: if convert list to single object, by default,
            the return value will return a objects list
        :param kwargs: params for filter, like django model's filter

        """
        if not isinstance(model, models.base.ModelBase):
            app_label, model_name = model.rsplit('.', 1)
            model = apps.get_model(app_label, model_name)

        if not model:
            return None

        instances = self.get_from_cache(model, connection_name,
                                        cache_name=cache_name, **kwargs)
        if flat:
            if instances:
                return instances[0]
            else:
                return None

        return instances
