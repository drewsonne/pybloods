import logging
import os
from urllib.parse import urljoin

from requests import Session


class ApiBaseClient(Session):
    def __init__(self, prefix_url=None, *args, **kwargs):
        super(ApiBaseClient, self).__init__(*args, **kwargs)
        self.prefix_url = prefix_url

    def request(self, method, url, *args, **kwargs):
        url = urljoin(self.prefix_url, url)
        return super(ApiBaseClient, self).request(method, url, *args, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def create(self, **attrs):
        return self._process_response(
            super(ApiBaseClient, self).post(self.prefix_url, json=attrs)
        )

    def get(self, **attrs):
        return self._process_response(
            super(ApiBaseClient, self).get(self.prefix_url, params=attrs)
        )

    def _process_response(self, response):
        if response.ok:
            try:
                return response.json()
            except Exception as e:
                return response.text
        return None

    @classmethod
    def config_logging(cls, logging_level='info'):
        try:
            import http.client as http_client
        except ImportError:
            # Python 2
            import httplib as http_client
        http_client.HTTPConnection.debuglevel = 1

        # You must initialize logging, otherwise you'll not see debug output.
        logging.basicConfig()
        logging.getLogger().setLevel(
            getattr(logging, logging_level.upper())
        )
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True


ApiBaseClient.config_logging(os.environ.get('PYBLOODS_LOGGING_LEVEL', 'info'))
