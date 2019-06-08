import connexion
from connexion import RestyResolver

from pybloods.model.orm import init_db


class CliHandler(object):
    instance = None

    @classmethod
    def cli(cls):
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance

    def __init__(self):
        self._db_session = init_db('sqlite:///:memory:')
        self._app = connexion.FlaskApp(__name__)
        self._app.add_api(
            'openapi/v1.yaml',
            resolver=RestyResolver('pybloods.api.handler')
        )

        @self._app.app.teardown_appcontext
        def shutdown_session(exception=None):
            self._db_session.remove()

    def start(self):
        self._app.run(port=8081, use_reloader=False, threaded=False)


def run():
    CliHandler.cli().start()
