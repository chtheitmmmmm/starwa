"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['media']
OPTIONS = {
    'iconfile': 'icon.icns',
    'includes': ['os', 'random', 'pygame', 'sys', 'abc']
}

setup(
    name            = "星野守望",
    app             = APP,
    version         = '0.5',
    author          = 'cmtheit',
    author_email    = 'cmtheit@outlook.com',

    data_files      = DATA_FILES,
    options         = {
        'py2app': OPTIONS
    },
    setup_requires  = ['py2app'],
)