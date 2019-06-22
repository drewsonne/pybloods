from pybloods.cli.handler import run, Context
import pybloods.cli.handler.observations


def cli():
    run(obj=Context())


if __name__ == '__main__':
    cli()
