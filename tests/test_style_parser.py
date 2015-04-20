#
# tests/test_style_parser.py
#

from pystylus.parser import (StylusParser, StylusParserError)
import pystylus.ast as AST
import pytest


def test_simple_style():
    s = """
div
  color red
"""
    res = StylusParser().parse(s)


def test_multi_style():
    s = """
div
  color red


body
  margin 0 0 30px 30px
"""
    res = StylusParser().parse(s)
