#
# tests/test_conditional_node.py
#

import pytest
import pystylus.lexer
import pystylus.parser


@pytest.fixture
def lexer():
    return pystylus.lexer.StylusLexer()


@pytest.fixture
def parser():
    return pystylus.parser.StylusParser()


@pytest.mark.parametrize("string, types", [
    ("x == y", ('NAME', 'WS', 'EQUALS', 'EQUALS', 'WS', 'NAME')),
    ("x == 0", ('NAME', 'WS', 'EQUALS', 'WS', 'NUMBER')),
])
def test_equality_lexing(lexer, string, types):
    t = lexer.tokenize(string)
    for token, type_ in zip(t, types):
        assert token.type == type_


# def test_equality_parsing(parser):
#     p = parser.parse("x and y")
#     assert p is None
