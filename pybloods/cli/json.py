import json


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

    def serializer(*args, **kwargs):
        r = f(*args, **kwargs)
        print(
            json.dumps(
                to_dict(r),
                indent=4
            )
        )

    return serializer
