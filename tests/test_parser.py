#
# tests/test_parser.py
#

from pystylus.parser import StylusParser
import pytest


def test_constructor():
    styl = StylusParser()


def test_block():
    s = "body"
    styl = StylusParser()
    styl.parse(s)
