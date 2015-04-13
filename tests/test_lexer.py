#
# tests/test_lexer.py
#

from pystylus.lexer import StylusLexer


def test_construction():

    lexer = StylusLexer()
    assert lexer
