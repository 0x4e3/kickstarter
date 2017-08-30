# coding=utf-8
from __future__ import unicode_literals, absolute_import

import click

from django.core.management import execute_from_command_line

from kickstarter.runner.decorators import configuration


@click.command(
    add_help_option=False, context_settings=dict(
        ignore_unknown_options=True,
    )
)
@click.argument('management_args', nargs=-1, type=click.UNPROCESSED)
@click.pass_context
@configuration()
def django(ctx, management_args, *args, **kwargs):
    """Execute Django subcommands."""
    execute_from_command_line(argv=[ctx.command_path] + list(management_args))
