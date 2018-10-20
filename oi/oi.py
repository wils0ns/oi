"""Oi command line parser module"""
from __future__ import print_function, absolute_import
import argparse


class BaseCommand(object):
    """Base command line object"""

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
        self.args = []

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
            argparse._SubParsersAction
        """
        if not self.sub_parser:
            self.sub_parser = self.parser.add_subparsers()
        return self.sub_parser

    def add_argument(self, *args, **kwargs):
        """
        Add arguments.

        Args:
            *args:
            **kwargs:

        See Also:
            https://docs.python.org/2/library/argparse.html#the-add-argument-method

        Returns:

        """
        self.args.append({'args': args, 'kwargs': kwargs})
        self.parser.add_argument(*args, **kwargs)

    def help_markdown(self):
        """
        Generates markdown code with all command arguments.

        Returns:
            str: [description]
        """

        markdown = '|Argument|Help|\n|-|-|\n'
        for arg in self.args:
            for param in arg['args']:
                if param.startswith('-'):
                    markdown += '|`{}`|{}|\n'.format('` `'.join(arg['args']), arg['kwargs'].get('help', ''))
                    break

        return markdown


class App(BaseCommand):
    """Main parser."""

    def __init__(self, name, **kwargs):
        """
        Create a CLI parser.

        Args:
            name (str): Application name.
            **kwargs: Parameters supported by argparse.ArgumentParser.

        See Also:
            https://docs.python.org/2/library/argparse.html#argumentparser-objects
        """
        super(App, self).__init__(
            name=name,
            cmd_type=BaseCommand.TYPE_APP,
            parser=argparse.ArgumentParser(prog=name, **kwargs)
        )

    def parse_args(self, *args, **kwargs):
        """Parses the command line arguments.

        Args:
            *args:
            **kwargs:

        Returns:
            argparse.Namespace:

        See Also:
            https://docs.python.org/2/library/argparse.html#the-parse-args-method

        """
        return self.parser.parse_args(*args, **kwargs)


class Command(BaseCommand):
    """Positional command argument parser."""

    ACTION_STORE = 'store'
    ACTION_STORE_CONST = 'store_const'
    ACTION_STORE_TRUE = 'store_true'
    ACTION_STORE_FALSE = 'store_false'
    ACTION_APPEND = 'append'
    ACTION_APPEND_CONST = 'append_const'
    ACTION_COUNT = 'count'
    ACTION_HELP = 'help'
    ACTION_VERSION = 'version'

    def __init__(self, parent, name, **kwargs):
        """
        Creates a positional command argument.

        Args:
            parent: To object to add this command to. Either an `App` or another `Command`.
            name: The argument name.
            kwargs: Parameters supported by argparse's parsers.
        """
        super(Command, self).__init__(
            name=name,
            cmd_type=BaseCommand.TYPE_COMMAND,
            parser=parent.command_group.add_parser(name, **kwargs)
        )
        if parent.type == BaseCommand.TYPE_COMMAND:
            self.parser.set_defaults(command='{0}_{1}'.format(parent.name, name))
        else:
            self.parser.set_defaults(command='{0}'.format(name))
