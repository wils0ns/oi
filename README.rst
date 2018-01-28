Oi - Simple command-line interface parser.
==========================================

This small python package implements a simple object-oriented layer on top of python's `argparse <https://docs.python.org/2/library/argparse.html>`_,
offering a more intuitive and easier way to build command-line interfaces.

Quick Start
-----------

Installing Oi package.
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pip install oicli

Usage example
~~~~~~~~~~~~~

Given the commands bellow:

.. code-block:: bash

    $ myapp user list
    $ myapp user add --name Wilson --email wilson@codeminus.org

The parser would look like this:

.. code-block:: python

    import oi

    app = oi.App('myapp')
    user_cmd = oi.Command(app, 'user')

    user_list_cmd = oi.Command(user_cmd, 'list')

    user_add_cmd = oi.Command(user_cmd, 'add')
    user_add_cmd.add_argument('--name')
    user_add_cmd.add_argument('--email')

    print(app.parse_args())

Running the application with the code above:

.. code-block:: bash

    $ myapp user
    Namespace(command='user')

.. code-block:: bash

    $ myapp user list
    Namespace(command='user_list')

.. code-block:: bash

    $ myapp user add --name Wilson --email wilson@codeminus.org
    Namespace(command='user_add', email='wilson@codeminus.org', name='Wilson')


Notice the **command** attribute of the Namespace.
It correspond to the name of the command invoked.
The sub-command name is appended to its parent command to ensure a unique identifier is created.

What does "Oi" mean? Well... What does it mean to you? Try the `wiki <https://en.wikipedia.org/wiki/Oi_(interjection)>`_.

