import json
import pprint

from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyEncoder(json.JSONEncoder):

    @classmethod
    def to_dict(cls, obj):
        # an SQLAlchemy class
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                json.dumps(data)  # this will fail on non-encodable values, like other classes
                fields[field] = data
            except TypeError:
                fields[field] = None
        # a json-encodable dict
        return fields

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            return AlchemyEncoder.to_dict(obj)
        return json.JSONEncoder.default(self, obj)


def dictify(obj_list):
    return [
        AlchemyEncoder.to_dict(orm)
        for orm
        in obj_list
    ]


def jsonify(data):
    try:
        json.dumps(data, indent=4, cls=AlchemyEncoder)
    except Exception as e:
        pprint.PrettyPrinter(indent=4).pprint(data)
        print(str(e))
