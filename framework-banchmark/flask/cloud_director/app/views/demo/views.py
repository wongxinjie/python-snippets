# coding: utf-8
from flask import jsonify, request
from flask.views import MethodView

from app.views.demo import demo
from app.services.handlers import apply_seqver


@demo.route('/func-apply-seqver', methods=['GET', 'POST'])
def func_apply_view():

    if request.method == 'POST':
        seqver = apply_seqver()
        kw = {'seqver': seqver}
    else:
        kw = {"msg": "greeting from flask function-base view"}

    return jsonify(kw)


class ApplyView(MethodView):

    def get(self):
        kw = {"msg": "greeting from flask class base view"}
        return jsonify(kw)

    def post(self):
        seqver = apply_seqver()
        kw = {'seqver': seqver}
        return jsonify(kw)

demo.add_url_rule('/class-apply-seqver',
                  view_func=ApplyView.as_view('class_apply_view'))
