#
# setup.py
#
"""
A pure-python stylus to CSS converter
"""

from setuptools import setup

import pystylus

PLATFORMS = 'all'

REQUIRES = [
    'ply==3.4',
]

CLASSIFIERS = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
]

setup(
    name='pystylus',
    packages=['pystylus', 'pystylus.parsing_rules'],
    scripts=['scripts/pystylus'],
    version=pystylus.__version__,
    author=pystylus.__author__,
    author_email=pystylus.__contact__,
    license=pystylus.__license__,
    url=pystylus.__url__,
    platforms=PLATFORMS,
    install_requires=REQUIRES,
    classifiers=CLASSIFIERS,
)
