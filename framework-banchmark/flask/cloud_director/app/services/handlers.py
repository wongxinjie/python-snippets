# coding: utf-8
import uuid

from sqlalchemy import desc

from app.models.demo import Seqver


def apply_seqver():
    uid = str(uuid.uuid4())
    model = Seqver.query.order_by(desc(Seqver.created_on)).first()
    if model:
        seqver_num = model.seqver + 1
    else:
        seqver_num = 0

    model = Seqver(seqver=seqver_num, uuid=uid)
    model.save()
    return model.seqver
