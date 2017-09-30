from __future__ import print_function, absolute_import
import argparse


class App(object):
    """CLI parser"""

    def __init__(self, name, **kwargs):
        """
        Create a CLI parser.

        Args:
            name (str): Application name.
            kwargs (dict): Dictionary of parameters supported by argparse.ArgumentParser.
        """
        self.name = name
        self._type = 'app'
        self.parser = argparse.ArgumentParser(prog=name, **kwargs)
        self.sub_parser = None

    @property
    def type(self):
        """
        The command type.

        Returns:
            str
        """
        return self._type

    @property
    def command_group(self):
        """
        Returns the sub parser of the application.

        Returns:

        """
        if not self.sub_parser:
            self.sub_parser = self.parser.add_subparsers()
        print(type(self.sub_parser))
        return self.sub_parser


class Command(object):
    def __init__(self, parent, name):
        self.name = name
        self._type = 'command'
        self.parser = parent.command_group.add_parser(name)
        if parent.type == 'command':
            self.parser.set_defaults(command='{0}_{1}'.format(parent.name, name))
        else:
            self.parser.set_defaults(command='{0}'.format(name))
        self.sub_parser = None

    @property
    def type(self):
        return self._type

    @property
    def command_group(self):
        if not self.sub_parser:
            self.sub_parser = self.parser.add_subparsers()
        return self.sub_parser

    def add_argument(self, *args, **kwargs):
        self.parser.add_argument(*args, **kwargs)