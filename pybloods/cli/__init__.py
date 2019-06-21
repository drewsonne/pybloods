import click

import pybloodsclient
from pybloodsclient import Configuration


@click.group()
@click.option('--server', default='http://localhost:5000')
@click.option('--api-version', default=1, type=int)
@click.pass_context
def run(ctx, server, api_version):
    cfg = Configuration()
    cfg.host = "http://127.0.0.1:5000/api/v1"
    cfg.host = f'{server}/api/v{api_version}'

    ctx.obj['client'] = pybloodsclient.DefaultApi(
        pybloodsclient.ApiClient(cfg)
    )


@run.group()
@click.pass_context
def observations(ctx): pass


@observations.command()
@click.option('--observation-ids', default=[])
@click.pass_context
def get(ctx, observation_ids):
    # create an instance of the API class

    print(
        ctx.obj['client'].pet.getPetById(petId=42).response().result
    )


@observations.command('create')
@click.option('--value', required=True, type=float)
@click.option('--unit', required=True)
@click.option('--extraction-date', required=True)
@click.pass_context
def create(ctx, value, unit, extraction_date):
    ctx.obj['client'].observations.addPet(body=pet).response().result
    # create_observation(ctx, value, unit, extraction_date)


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


def cli():
    run(obj={}, client=None)


if __name__ == '__main__':
    cli()
