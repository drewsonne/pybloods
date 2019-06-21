from pybloods.api import ApiApp
from pybloods.api.response import dictify
from pybloods.model.orm import Observation


def search():
    return dictify(
        ApiApp.
            db().
            query(Observation).
            all()
    )


def post(body):
    db = ApiApp.db()
    o = Observation(**body)
    db.add(o)
    db.commit()

    return None, 301, {
        'Location': '/api/v1/observation/' + o.observation_id
    }
