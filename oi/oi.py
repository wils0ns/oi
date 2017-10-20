from __future__ import print_function, absolute_import
import argparse


class BaseCommand(object):
    TYPE_APP = 'app'
    TYPE_COMMAND = 'command'

    def __init__(self, name, cmd_type, parser):
        """

        Args:
            name (str): Command name.
            cmd_type (str): Command type.
            parser: argparse's parser object.
        """
        self.name = name
        self._type = cmd_type
        self.parser = parser
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
        return self.sub_parser

    def add_argument(self, *args, **kwargs):
        """
        Add optional arguments.

        Args:
            *args:
            **kwargs:

        See Also:
            argparse.parser.add_argument()

        Returns:

        """
        self.parser.add_argument(*args, **kwargs)


class App(BaseCommand):
    """Main parser."""

    def __init__(self, name, **kwargs):
        """
        Create a CLI parser.

        Args:
            name (str): Application name.
            kwargs: Parameters supported by argparse.ArgumentParser.
        """
        super(App, self).__init__(
            name=name,
            cmd_type=BaseCommand.TYPE_APP,
            parser=argparse.ArgumentParser(prog=name, **kwargs)
        )

    def parse_args(self, *args, **kwargs):
        return self.parser.parse_args(*args, **kwargs)


class Command(BaseCommand):
    """Positional command argument parser."""
    def __init__(self, parent, name):
        """
        Creates a positional command argument.

        Args:
            parent: To object to add this command to. Either an `App` or another `Command`.
            name: The argument name.
        """
        super(Command, self).__init__(
            name=name,
            cmd_type=BaseCommand.TYPE_COMMAND,
            parser=parent.command_group.add_parser(name)
        )
        if parent.type == BaseCommand.TYPE_COMMAND:
            self.parser.set_defaults(command='{0}_{1}'.format(parent.name, name))
        else:
            self.parser.set_defaults(command='{0}'.format(name))
