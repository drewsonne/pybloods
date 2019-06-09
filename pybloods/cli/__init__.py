import click

from pybloods.cli.client import ApiClient, api_client
from pybloods.cli.handler.observations import create as create_observation


@click.group()
@click.option('--server', default='http://localhost:5000/api/v1')
@click.pass_context
def run(ctx, server):
    ctx.obj['server'] = server


@run.group()
@click.pass_context
def observations(ctx): pass


@observations.command()
@click.option('--observation-ids', default=[])
@click.pass_context
@api_client
def get(client, observation_ids):
    observations.get(client, observation_ids)


@observations.command('create')
@click.option('--value', required=True, type=float)
@click.option('--unit', required=True)
@click.option('--extraction-date', required=True)
@click.pass_context
def create(ctx, value, unit, extraction_date):
    create_observation(ctx, value, unit, extraction_date)


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
    run(obj={})


if __name__ == '__main__':
    cli()
