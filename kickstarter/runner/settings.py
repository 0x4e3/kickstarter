# coding=utf-8
from __future__ import unicode_literals

import os
import sys

import click
import django
from django.core.exceptions import ImproperlyConfigured

from kickstarter.importer import Importer


GUNICORN_SETTINGS_MODULE = 'kickstarter.conf.web'
CELERY_WORKER_SETTINGS_MODULE = 'kickstarter.conf.worker'
CELERY_BEAT_SETTINGS_MODULE = 'kickstarter.conf.beat'
DJANGO_SETTINGS_MODULES = {
    'production': 'kickstarter.config.settings.production',
    'local': 'kickstarter.config.settings.local'
}


def discover_config():
    """
    Discovers services configs and settings.
    """
    pass


def configure(ctx, settings):
    """
    Sets up the environment.

    NOTE: Uses global flag to prevent multiple executions.
    """
    global __configured
    if __configured:
        return

    os.environ['DJANGO_SETTINGS_MODULE'] = 'project_settings'
    settings_module = DJANGO_SETTINGS_MODULES[settings]
    settings_file = '{}.py'.format(settings_module.replace('.', '/'))
    settings_path = os.path.abspath(settings_file)

    if not os.path.exists(settings_path) or not os.path.isfile(settings_path):
        if ctx:
            raise click.ClickException(
                'Settings file {} does not exists.'.format(settings_path))
        raise ImproperlyConfigured(
            'Settings file {} does not exists.'.format(settings_path))

    sys.meta_path.append(
        Importer('project_settings', settings_path, settings_module))
    django.setup()

    __configured = True


__configured = False
