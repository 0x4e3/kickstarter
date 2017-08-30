# coding=utf-8
from __future__ import unicode_literals, absolute_import

import functools
import os

import click

from kickstarter.runner.settings import configure

LOG_LEVELS = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL', 'FATAL')


class CaseInsensitiveChoice(click.Choice):
    def convert(self, value, param, ctx):
        self.choices = [choice.upper() for choice in self.choices]
        return super(CaseInsensitiveChoice).convert(value.upper(), param, ctx)


def log_command_options(default=None):
    def wrapper(func):
        @click.pass_context
        @click.option(
            '--log-level',
            '-l',
            default=default,
            help='Global logging level.',
            envvar='DJANGO_LOG_LEVEL',
            type=CaseInsensitiveChoice(LOG_LEVELS)
        )
        @functools.wraps(func)
        def inner(ctx, log_level=None, *args, **kwargs):
            if log_level:
                os.environ['DJANGO_LOG_LEVEL'] = log_level
            return ctx.invoke(func, *args, **kwargs)
        return inner
    return wrapper


def configuration():
    def wrapper(func):
        @click.pass_context
        @click.option(
            '--settings',
            '-S',
            default='local',
            help='Project settings: "local", "production".',
            type=click.Choice(['local', 'production'])
        )
        @functools.wraps(func)
        def inner(ctx, *args, **kwargs):
            # TODO(ad): Maybe we'll need to bypass the initialization here.
            configure(ctx, kwargs.pop('settings'))
            return ctx.invoke(func, *args, **kwargs)
        return inner
    return wrapper
