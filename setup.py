#
# setup.py
#
"""
A pure-python stylus to CSS converter
"""

from setuptools import setup

import pystylus
from pystylus import tokens

PLATFORMS = 'all'

REQUIRES = [
    'ply',
]

setup(
    name='pystylus',
    packages=['pystylus'],
    scripts=['scripts/pystylus'],
    version=pystylus.__version__,
    author=pystylus.__author__,
    author_email=pystylus.__contact__,
    license=pystylus.__license__,
    url=pystylus.__url__,
    platforms=PLATFORMS,
    install_requires=REQUIRES,
)
