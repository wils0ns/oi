Oi - Simple command-line interface parser.
==========================================

This small python package implements a simple object-oriented layer on top of python's *argparse*,
offering a more intuitive and easier way to build command-line interfaces.

Why "Oi"? Why not?

What does it mean? Well... What does it mean to you? Try https://en.wikipedia.org/wiki/Oi_(interjection)


Quick Start
-----------

Installing Oi package.
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    pip install oicli

Usage example
~~~~~~~~~~~~~

myapp user list

myapp user add --name Wilson --email wilson@codeminus.org


.. code-block:: python

    import oi

    app = oi.App('myapp')
    user_cmd = oi.Command(app, 'user')

    user_list_cmd = oi.Command(user_cmd, 'list')

    user_add_cmd = oi.Command(user_cmd, 'add')
    user_add_cmd.add_argument('--name')
    user_add_cmd.add_argument('--email')

    print(app.parse_args())
