#
# tests/test_parser.py
#

from pystylus.parser import StylusParser
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
    s = "A(a,b,c)"
    styl = StylusParser()
    styl.parse(s)
    # assert styl.stack[0] == 1


if __name__ == '__main__':
    test_block()
