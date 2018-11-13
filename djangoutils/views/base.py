# -*- coding: utf-8 -*-

from django.http import JsonResponse
from django.views.generic.edit import BaseFormView
from django.views.generic.edit import UpdateView


class JsonResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )


class PostView(BaseFormView):

    def get(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)
