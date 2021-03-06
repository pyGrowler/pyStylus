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


def test_selector_list():
    s = "div,body\n background blue"
    res = StylusParser().parse(s)

    s = "div\nbody\n background blue"
    res = StylusParser().parse(s)
    assert isinstance(res[0], AST.StyleNode)
    assert str(res[0]) == "div, body{background:blue}"


def test_universal_selector():
    s = "*\n color red"
    res = StylusParser().parse(s)
    assert isinstance(res[0], AST.StyleNode)
    assert res[0].selectors[0] == '*'
