# coding=utf-8
from __future__ import unicode_literals, absolute_import

import click

from django.core.management import call_command


@click.command()
@click.option('--verbosity', '-v', default=1, help='Verbosity level.')
@click.option('--traceback', default=True, is_flag=True,
              help='Raise on exception.')
@click.option('--no-input', default=False, is_flag=True,
              help='Do not prompt the user for input of any kind.')
@click.pass_context
def upgrade(ctx, verbosity, traceback, no_input):
    """Perform any pending database migrations and upgrades."""
    interactive = not no_input
    call_command(
        'syncdb',
        interactive=interactive,
        traceback=traceback,
        verbosity=verbosity)
    call_command(
        'migrate',
        merge=True,
        ignore_ghost_migrations=True,
        interactive=interactive,
        traceback=traceback,
        verbosity=verbosity)
