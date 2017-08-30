# coding=utf-8
from __future__ import unicode_literals

import os

from django.core.management import find_commands
from django.utils.module_loading import import_string


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def load_command_class(app_name, name):
    """
    Return command instance by given application name and command name.
    """
    return import_string(
        '{0}.runner.commands.{1}.{1}'.format(app_name, name))


class Commander(object):
    def __init__(self, cli):
        self.cli = cli

    def _load_kickstarter_commands(self):
        command_dir = os.path.join(BASE_DIR, 'runner')
        command_names = find_commands(command_dir)
        commands = list(map(
            lambda cmd: load_command_class('kickstarter', cmd),
            command_names))
        for command in commands:
            self.cli.add_command(command)

    def add_commands(self):
        self._load_kickstarter_commands()
