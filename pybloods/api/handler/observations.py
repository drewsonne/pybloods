import moment

from pybloods.api import ApiApp
from pybloods.api.response import dictify
from pybloods.model.orm import Observation


def search():
    result = ApiApp.db().query(Observation)

    return dictify(result)


def post(body):
    if 'extracted_at' in body:
        body['extracted_at'] = moment.date(body['extracted_at']).datetime

    db = ApiApp.db()
    o = Observation(**body)
    db.add(o)
    db.commit()

    return o.to_dict(), 201
