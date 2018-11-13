# coding: utf-8

from  flask import Blueprint

demo = Blueprint('demo', __name__)

from .views import func_apply_view
