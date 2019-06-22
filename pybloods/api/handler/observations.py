import moment

from pybloods.api import ApiApp
from pybloods.api.response import dictify
from pybloods.model.orm import Observation


def search():
    observations = ApiApp.db().query(Observation)

    return dictify(observations)


def post(body):
    if 'extracted_at' in body:
        body['extracted_at'] = moment.date(body['extracted_at']).datetime

    db = ApiApp.db()
    observation = Observation(**body)
    db.add(observation)
    db.commit()

    return dictify(observation), 201
