"""Package setup"""
from os import path
from codecs import open
from setuptools import setup, find_packages

THIS_FOLDER = path.abspath(path.dirname(__file__))

# Get package version from .version file
with open(path.join(THIS_FOLDER, '.version')) as f:
    VERSION = f.read()

# Get long description from README.rst file
with open(path.join(THIS_FOLDER, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='oicli',
    version=VERSION,
    author='Wilson Santos',
    author_email='wilson@codeminus.org',
    url='https://gitlab.com/cathaldallan/oi',
    description='Simple command-line parser.',
    long_description=LONG_DESCRIPTION,
    license='MIT',
    keywords='cli argparse command-line interface',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(exclude=['docs', 'tests']),
)
