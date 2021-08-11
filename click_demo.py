import sys
import os
import inspect
from pprint import pprint as pp

import dotenv
import click


# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo(f"Hello {name}!")
#
#
# if __name__ == '__main__':
#     hello()


# 使用方式
# python click_demo.py
# python click_demo.py --count=3
# python click_demo.py --help


@click.group()
def cli():
    pass


@click.command()
def checkenv(*args, **kwargs):
    click.echo('checkenv')
    # click.echo(sys.argv[1:])
    # pp(list(os.environ.items()))
    sig = inspect.signature(checkenv)
    print(sig)


@click.command()
def dropdb():
    click.echo('Dropped the database')


@click.command()
def loaddotenv():
    click.echo('loaddotenv')
    pp(dotenv.load_dotenv())
    gcp_project_id = os.getenv('GCP_PROJECT_ID')
    service_account_file = os.getenv('SERVICE_ACCOUNT_FILE')
    storage_bucket_name = os.getenv('STORAGE_BUCKET_NAME')
    print(gcp_project_id, service_account_file, storage_bucket_name)


cli.add_command(checkenv)
cli.add_command(dropdb)
cli.add_command(loaddotenv)

if __name__ == '__main__':
    cli()
