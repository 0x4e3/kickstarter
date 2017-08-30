# coding=utf-8
from __future__ import unicode_literals, absolute_import

import six

from gunicorn.app.base import BaseApplication

from django.core.wsgi import get_wsgi_application


class HttpService(BaseApplication):
    def __init__(self, options=None):
        self.options = options or {}
        self.application = get_wsgi_application()
        super(HttpService, self).__init__()

    def load(self):
        return self.application

    def load_config(self):
        config = dict([(key, value) for key, value
                       in six.iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in six.iteritems(config):
            self.cfg.set(key.lower(), value)
