#
# tests/test_parser.py
#

from pystylus.parser import (StylusParser, StylusParserError)
import pystylus.ast as AST
import pytest


def test_constructor():
    styl = StylusParser()


def test_block():
    s = "body\ndiv"
    styl = StylusParser()
    styl.parse(s)
    print(styl.stack)
    assert styl.stack[0]['selector'] == 'body'
    assert styl.stack[1]['selector'] == 'div'


def test_function_definition():
    s = "A(a, b,c)"
    styl = StylusParser()
    styl.parse(s)
    func = styl.stack[0]
    assert type(func) == AST.Function
    assert func.name == 'A'
    assert func.args == ['a', 'b', 'c']


def test_bad_function_definition():
    with pytest.raises(StylusParserError):
        StylusParser().parse("A (a, b,c)")


def xtest_function_block():
    s = """add(x, y)
    x + y
"""
    styl = StylusParser()
    styl.parse(s)


if __name__ == '__main__':
    test_block()
