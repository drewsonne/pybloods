import click

from pybloodsclient import Configuration, DefaultApi, ApiClient


class Context(object):
    client = None


@click.group()
@click.option('--server', default='http://localhost:8081')
@click.option('--api-version', default=1, type=int)
@click.pass_context
def run(ctx, server, api_version):
    cfg = Configuration()
    cfg.host = "http://127.0.0.1:5000/api/v1"
    cfg.host = f'{server}/api/v{api_version}'

    ctx.obj.client = DefaultApi(
        ApiClient(cfg)
    )


@run.group()
@click.pass_context
def note_groups(ctx): pass


@run.group()
@click.pass_context
def providers(ctx): pass


@run.group()
@click.pass_context
def samples(ctx): pass


@run.group()
@click.pass_context
def sources(ctx): pass


@run.group()
@click.pass_context
def units(ctx): pass
