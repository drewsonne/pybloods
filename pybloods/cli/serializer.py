import json
from datetime import date, datetime


def as_json(f):
    def to_dict(o):
        if type(o) in [list, tuple]:
            return [
                to_dict(e)
                for e
                in o
            ]
        if hasattr(o, 'to_dict'):
            return o.to_dict()

        return o

    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError("Type %s not serializable" % type(obj))

    def serializer(*args, **kwargs):
        r = f(*args, **kwargs)
        print(
            json.dumps(
                to_dict(r),
                indent=4,
                default=json_serial
            )
        )
        return r

    return serializer
