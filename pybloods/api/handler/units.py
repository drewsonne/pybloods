from pybloods.api import ApiApp
from pybloods.api.response import dictify
from pybloods.model.orm import Unit


def search(name=None):
    result = ApiApp.db().query(Unit)
    if name is not None:
        result = result.filter_by(name=name)

    return dictify(result)


def post(body):
    db = ApiApp.db()
    u = Unit(**body)
    db.add(u)
    db.commit()

    return dictify(u), 201
