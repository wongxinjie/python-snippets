#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class JsonTemplateResponse(JsonResponse):

    def __init__(self, result_status, result, **kwargs):
        data = {
            "status": result_status,
            "result": result
        }
        super(JsonTemplateResponse, self).__init__(
                data=data, safe=False, **kwargs)


class JsonSuccessResponse(JsonResponse):

    def __init__(self):
        data = {
            "status": "ok"
        }
        super(JsonSuccessResponse, self).__init__(
                data=data, safe=False)


class JsonLoginRequiredMixin(LoginRequiredMixin):

    def handle_no_permission(self):
        return JsonTemplateResponse(1001, u"用户未登录", status=403)
