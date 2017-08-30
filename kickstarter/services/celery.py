# coding=utf-8
from __future__ import unicode_literals, absolute_import

from celery import Celery
from raven import Client
from raven.contrib.celery import register_signal, register_logger_signal

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class CeleryApp(Celery):
    def on_configure(self):
        if not settings.DEBUG:
            try:
                client = Client(settings.RAVEN_CONFIG['dsn'])
            except (KeyError, AttributeError, ImproperlyConfigured):
                raise ImproperlyConfigured(
                    'Project uses raven for logging to Sentry. '
                    'Please, specify `RAVEN_CONFIG` namespace '
                    'with valid `dsn` key in your settings.py')
            register_logger_signal(client)
            register_signal(client)

app = CeleryApp('kickstarter')
app.config_from_object(settings)
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
