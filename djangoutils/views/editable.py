# -*- coding: utf-8 -*-
import json

from django.core import exceptions as django_exceptions
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.list import BaseListView

from apps.utils.views.base import JsonResponseMixin


class SingleValueEditableView(View):
    """Xeidtable api view to update single value for the model.

    - **parameters**, **types**, **return** and **return types**::

        :attr model(django.db.models.Model) The Model for updating.
    """
    model = None

    def dispatch(self, *args, **kwargs):
        return super(SingleValueEditableView, self).dispatch(*args, **kwargs)

    def post(self, *args, **kwargs):
        post_data = self.request.POST.dict()
        self.pk = post_data.get('pk')
        self.key = post_data.get('name')
        self.value = post_data.get('value')
        self.instance, error = self.get_instance(self.pk)

        if not self.instance:
            return HttpResponse(error, status=404)

        success, error = self.set_instance_value(self.key, self.value)
        if not success:
            return HttpResponse(error, status=400)

        success, error = self.save_instance()
        if not success:
            return HttpResponse(error, status=400)

        return HttpResponse('success')

    def get_instance(self, pk):
        try:
            instance = self.model.objects.get(pk=pk)
        except django_exceptions.ValidationError:
            return None, 'Object does not exists.'
        return instance, 'success'

    def set_instance_value(self, key, value):
        if not hasattr(self.instance, key):
            return False, 'No such attribute.'
        setattr(self.instance, key, value)
        return True, 'success'

    def save_instance(self):
        try:
            self.instance.save()
        except django_exceptions.ValidationError:
            return False, 'Value "%s" is invalid.' % self.value
        return True, 'success'


class EditableDataTableListView(JsonResponseMixin, BaseListView):

    model = None
    more_attrs = []

    def parse_datatable_infos(self):
        datas = self.request.GET.dict()
        del(datas['_'])
        raw_datas = json.loads(list(datas.keys())[0])
        columns = raw_datas['columns']
        order_by = columns[raw_datas['order'][0]['column']]['name']
        if raw_datas['order'][0]['dir'] != 'asc':
            order_by = '-' + order_by

        if not order_by:
            order_by = 'id'

        datas = {
            'start': raw_datas['start'],
            'length': raw_datas['length'],
            'columns': raw_datas['columns'],
            'order_by': order_by,
        }
        return datas

    def get_context_data(self, **kwargs):
        context = super(EditableDataTableListView, self
                        ).get_context_data(**kwargs)
        table_infos = self.parse_datatable_infos()
        start = table_infos['start']
        length = table_infos['length']
        object_list = context['object_list'].order_by(table_infos['order_by'])
        page_object_list = object_list[start:start + length]
        total = object_list.count()

        data = []
        for obj in page_object_list:
            obj_data = model_to_dict(obj)
            fields = obj._meta.get_fields()
            for field in fields:
                if field.choices:
                    key = 'get_%s_display' % field.name
                    obj_data[key] = getattr(obj, key)()

            for attr in self.more_attrs:
                if hasattr(obj, attr):
                    obj_data[attr] = getattr(obj, attr)

            data.append(obj_data)

        context.update({
            'total': total,
            'filter_total': total,
            'data': data,
        })
        return context

    def get_data(self, context):
        datas = {
            'data': context['data'],
            'recordsTotal': context['total'],
            'recordsFiltered': context['filter_total'],
        }
        return datas
