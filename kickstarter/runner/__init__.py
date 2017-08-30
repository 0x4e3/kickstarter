# coding=utf-8
from __future__ import unicode_literals

import click

from kickstarter.management import Commander


@click.group()
@click.pass_context
def cli(ctx):
    pass

# Discovers kickstarter's management commands.
commander = Commander(cli)
commander.add_commands()


def main():
    cli(prog_name='kickstarter')
