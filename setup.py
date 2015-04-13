#
# setup.py
#
"""
A pure-python stylus to CSS converter
"""

from setuptools import setup

import pystylus

from pystylus import tokens

REQUIRES = [
    'ply',
]

print(tokens)

setup(
    name='pystylus',
    version=pystylus.__version__,
    author=pystylus.__author__,
    author_email=pystylus.__contact__,
    license=pystylus.__license__,
    url=pystylus.__url__,
    packages=['pystylus'],
    platforms='all',
)
