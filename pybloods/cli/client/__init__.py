import click

from pybloods.cli.client.base import ApiBaseClient


class ApiClient(ApiBaseClient):
    @property
    def observations(self):
        return ApiClient(
            prefix_url=self.prefix_url + '/observations'
        )

    @property
    def units(self):
        return ApiClient(
            prefix_url=self.prefix_url + '/units'
        )

def api_client(func):
    def wrapper(ctx, *args, **kwargs):
        with ApiClient(ctx.obj['server']) as client:
            func(client, *args, *kwargs)
    return wrapper
