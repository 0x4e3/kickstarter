# coding=utf-8
from __future__ import unicode_literals

import sys
import click

from multiprocessing import cpu_count

from kickstarter.runner.decorators import log_command_options, configuration
from kickstarter.runner.utils import call_command
from kickstarter.services import http, celery
from kickstarter.utils.click import AddressParamType as Address


@click.group()
def run():
    """
    Run a service.
    """


@run.command()
@click.option('--bind', '-b', default=None,
              help='Bind address.', type=Address())
@click.option('--workers', '-w', default=0,
              help='The number of worker processes for handling requests.')
@click.option('--upgrade', default=False, is_flag=True,
              help='Upgrade before starting.')
@click.option('--noinput', default=False, is_flag=True,
              help='Do not prompt the user for input of any kind.')
@log_command_options()
@configuration()
def web(bind, workers, upgrade, noinput):
    """
    Runs gunicorn instance.
    """
    if upgrade:
        click.echo('Performing upgrade before gunicorn startup.')
        try:
            call_command(
                'kickstarter.runner.commands.upgrade.upgrade',
                verbosity=0,
                noinput=noinput)
        except click.ClickException:
            raise
    options = {'host': bind[0], 'port': bind[1], 'workers': workers}
    http.HttpService(options=options).run()


@run.command()
@click.option('--hostname', '-n',
              help=('Set custom hostname, e.g. \'w1.%h\'. Expands: %h'
                    '(hostname), %n (name) and %d, (domain).'))
@click.option('--concurrency', '-c', default=cpu_count(),
              help=('Number of child processes processing the queue. The '
                    'default is the number of CPUs available on your '
                    'system.'))
@click.option('--logfile', '-f',
              help='Path to log file. If no logfile is specified, '
                   'stderr is used.')
@click.option('--autoreload', is_flag=True, default=False,
              help='Enable auto reloading.')
@log_command_options()
@configuration()
def worker(**options):
    """
    Runs celery worker instance.
    """
    celery_worker = celery.app.Worker(pool_cls='processes', **options)
    celery_worker.start()
    try:
        sys.exit(celery_worker.exitcode)
    except AttributeError:
        pass


@run.command()
@click.option('--pidfile',
              help=('Optional file used to store the process pid. '
                    'The program will not start if this file already exists '
                    'and the pid is still alive.'))
@click.option('--logfile', '-f',
              help=('Path to log file. If no logfile is specified, '
                    'stderr is used.'))
@click.option('--autoreload', is_flag=True, default=False,
              help='Enable auto reloading.')
@log_command_options()
@configuration()
def beat(**options):
    """
    Runs celery-beat - periodic task dispatcher.
    """
    celery.app.Beat(**options).run()
