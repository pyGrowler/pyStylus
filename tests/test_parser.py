#
# tests/test_parser.py
#

from pystylus.parser import (StylusParser, StylusParserError)
import pystylus.ast as AST
import pytest


def test_constructor():
    styl = StylusParser()
    assert isinstance(styl, StylusParser)


def test_block():
    s = "body\ndiv\n color red"
    styl = StylusParser()
    styl.parse(s)


def test_funcdef_no_args():
    s = 'foo()\n return'
    StylusParser().parse(s)


def test_function_definition():
    s = "foo(a, b,c)\n return a"
    styl = StylusParser()
    styl.parse(s)
    func = styl.stack[0]
    assert type(func) == AST.FunctionNode
    assert func.name == 'foo'
    assert func.args == ['a', 'b', 'c']


def test_bad_function_definition():
    with pytest.raises(StylusParserError):
        StylusParser().parse("A (a, b,c)\n return")


def test_empty_function():
    with pytest.raises(StylusParserError):
        StylusParser().parse("A(a)\n")


def xtest_function_block():
    s = """add(x, y)
    x + y
"""
    styl = StylusParser()
    styl.parse(s)


def test_if_node():
    s = "if x\n Do\n  Not Fail"
    toks = StylusParser().parse(s)
    assert isinstance(toks[0], AST.ConditionalNode)

    s = "if (x)\n Do\n  Not Fail"
    toks = StylusParser().parse(s)
    assert isinstance(toks[0], AST.ConditionalNode)


def test_if_else_node():
    s = "if x\n Do\n  Not Fail\nelse\n A\n  B C"
    toks = StylusParser().parse(s)
    assert isinstance(toks[0], AST.ConditionalNode)

    s = "if x\n Do\n  Not Fail\n\nelse\n   A\n    B C"
    toks = StylusParser().parse(s)
    assert isinstance(toks[0], AST.ConditionalNode)


def test_if_elif_node():
    s = "if x\n Do\n  Not Fail\nelif y\n A\n  B C"
    toks = StylusParser().parse(s)
    assert isinstance(toks[0], AST.ConditionalNode)

    s = "if x\n Do\n  Not Fail\n\nelif (y)\n   A\n    B C"
    toks = StylusParser().parse(s)
    assert isinstance(toks[0], AST.ConditionalNode)

    s = "if x\n Do\n  Not Fail\n\nelif (y)\n   A\n    B C\nelif a\n A\n  B C"
    toks = StylusParser().parse(s)
    assert isinstance(toks[0], AST.ConditionalNode)
    assert len(toks[0].else_ifs) == 2


def test_if_elif_else_node():
    s = "if x\n Do\n  Not Fail\nelif y\n A\n  B C\nelse\n q\n  q q"
    toks = StylusParser().parse(s)
    assert isinstance(toks[0], AST.ConditionalNode)
    assert len(toks[0].else_ifs) == 1


if __name__ == '__main__':
    test_block()
