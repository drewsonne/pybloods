import connexion
from connexion import RestyResolver

from pybloods.model.orm import init_db


class ApiApp(object):
    _instance = None

    @classmethod
    def api(cls):
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    @classmethod
    def db(cls):
        return cls.api()._db_session

    def __init__(self):
        self._db_session = init_db('sqlite:///pybloods.db')
        self._app = connexion.FlaskApp(__name__)
        self._app.add_api(
            'openapi/v1.yaml',
            resolver=RestyResolver('pybloods.api.handler')
        )

        @self._app.app.teardown_appcontext
        def shutdown_session(exception=None):
            self._db_session.remove()

    def start(self):
        self._app.run(port=8081)

    @property
    def app(self):
        return self._app.app


def run():
    ApiApp.api().start()


if __name__ == '__main__':
    run()
