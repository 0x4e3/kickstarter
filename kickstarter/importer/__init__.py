# coding=utf-8
from __future__ import unicode_literals

import sys
from importlib import import_module


class Importer(object):
    def __init__(self, name, file_path, module_path):
        self.name = name
        self.path = file_path
        self.module = module_path

    def find_module(self, filename, path=None):
        if filename != self.name:
            return
        return self

    def load_module(self, fullname):
        if fullname in sys.modules:
            return sys.modules[fullname]
        self.module = import_module(self.module)
        sys.modules[fullname] = self.module
        return self.module
