#
# tests/test_parser.py
#

from pystylus.parser import (StylusParser, StylusParserError)
import pystylus.ast as AST
import pytest


def test_constructor():
    """Test default constructor of StylusParser."""
    styl = StylusParser()
    assert isinstance(styl, StylusParser)


def test_block():
    """Parse a simple style rule."""
    s = "body\ndiv\n color red"
    styl = StylusParser()
    styl.parse(s)


@pytest.mark.parametrize("styl, arg_count", [
    ('foo()\n return', 0),
    ('foo(a, b,c)\n return a', 3)
])
def test_function_definition(styl, arg_count):
    """Parse a trivial function definition with multiple arguments"""
    func, = StylusParser().parse(styl)
    assert type(func) == AST.FunctionNode
    assert func.name == 'foo'
    assert len(func.args) == arg_count


def test_bad_function_definition():
    """Test bad function definition with space between name and bracket"""
    with pytest.raises(StylusParserError):
        StylusParser().parse("A (a, b,c)\n return")


def test_empty_function():
    """No empty function allowed"""
    with pytest.raises(StylusParserError):
        StylusParser().parse("A(a)\n")


def xtest_function_block():
    s = """add(x, y)
    x + y
"""
    styl = StylusParser()
    styl.parse(s)


@pytest.mark.parametrize("styl", [
    "if x\n Do\n  Not Fail",
    "if (x)\n Do\n  Not Fail"
])
def test_if_node(styl):
    """Test creation of ConditionalNode from simple if statement."""
    toks = StylusParser().parse(styl)
    assert len(toks) == 1
    assert isinstance(toks[0], AST.ConditionalNode)


@pytest.mark.parametrize("styl", [
    "if x\n Do\n  Not Fail\nelse\n A\n  B C",
    "if x\n Do\n  Not Fail\n\nelse\n   A\n    B C"
])
def test_if_else_node(styl):
    """Test creation of ConditionalNode from if+else statement."""
    toks = StylusParser().parse(styl)
    assert isinstance(toks[0], AST.ConditionalNode)


@pytest.mark.parametrize("styl, elif_count", [
    ("if x\n Do\n  Not Fail\nelif y\n A\n  B C", 1),
    ("if x\n Do\n  Not Fail\n\nelif (y)\n   A\n    B C", 1),
    ("if x\n Do\n  Not Fail\n\nelif (y)\n   A\n    B C\nelif a\n A\n  B C", 2),
])
def test_if_elif_node(styl, elif_count):
    """
    Test creation of ConditionalNode from if statement with variable number
    of elif statements.
    """
    toks = StylusParser().parse(styl)
    assert isinstance(toks[0], AST.ConditionalNode)
    assert len(toks[0].else_ifs) == elif_count


def test_if_elif_else_node():
    """Test creation of ConditionalNode from if+elif+else statement."""
    s = "if x\n Do\n  Not Fail\nelif y\n A\n  B C\nelse\n q\n  q q"
    toks = StylusParser().parse(s)
    assert isinstance(toks[0], AST.ConditionalNode)
    assert len(toks[0].else_ifs) == 1


if __name__ == '__main__':
    test_block()
