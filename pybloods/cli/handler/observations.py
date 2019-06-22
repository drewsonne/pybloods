import click

import pybloodsclient
from pybloods.cli.json import as_json
from pybloodsclient import NewUnit, NewObservation
from pybloods.cli import run


@run.group()
@click.pass_context
def observations(ctx): ...


@observations.command('get')
@click.option('--observation-ids', default=[])
@click.pass_context
@as_json
def get(ctx, observation_ids):
    client = ctx.obj.client  # type: pybloodsclient.DefaultApi

    return client.observations_get()


@observations.command('create')
@click.option('-v', '--value', required=True, type=float)
@click.option('-u', '--unit', required=True)
@click.option('-d', '--extraction-date', required=True)
@click.pass_context
@as_json
def create(ctx, value, unit, extraction_date):
    client = ctx.obj.client  # type: pybloodsclient.DefaultApi
    units = client.units_get(name=unit)
    unit = units[0] \
        if len(units) \
        else client.units_post(NewUnit(name=unit))

    return client.observations_post(
        NewObservation(
            extracted_at=extraction_date,
            value=value,
            unit_id=unit.unit_id
        )
    )
