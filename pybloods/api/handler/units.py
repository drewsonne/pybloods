from pybloods.api import ApiApp
from pybloods.api.response import dictify
from pybloods.model.orm import Unit


def search(name=None):
    print('units.search')
    result = ApiApp.db().query(Unit)
    if name is not None:
        result = result.filter_by(name=name)

    return dictify(result)


def post(body):
    db = ApiApp.db()
    u = Unit(name=body['name'])
    db.add(u)
    db.commit()

    return None, 301, {
        'Location': '/api/v1/unit/' + u.unit_id
    }
