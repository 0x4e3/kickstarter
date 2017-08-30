# coding=utf-8
from __future__ import unicode_literals

import click

from django.utils.module_loading import import_string

from kickstarter.exceptions import UnknownCommand


def call_command(name, obj=None, **kwargs):
    try:
        command = import_string(name)
    except (ImportError, AttributeError):
        raise UnknownCommand(name)

    with command.make_context('sentry', [], obj=obj or {}) as ctx:
        ctx.params.update(kwargs)
        try:
            command.invoke(ctx)
        except click.Abort:
            click.echo('Aborted!', err=True)
