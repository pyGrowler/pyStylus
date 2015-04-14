#
# tests/test_lexer.py
#

from pystylus.lexer import StylusLexer
import pytest


def test_construction():
    lexer = StylusLexer()
    assert lexer


def test_line():
    s = """This is a simple line"""
    lexer = StylusLexer()
    tokens = lexer.tokenize(s)
    for x in tokens[1:-2]:
        if x.type == 'WS':
            assert x.value == ' '
        assert x.type in ('NAME', 'WS')


def test_comment():
    s = """This has   // a comment"""
    # INDENT + NAME + WS + NAME + EOL + STYLUS_END
    assert len(StylusLexer().tokenize(s)) == 6


def test_tab_expansion():
    s = "\t"
    assert StylusLexer().tokenize(s)[0].type == 'INDENT'
    assert StylusLexer().tokenize(s)[0].value == ' '*8
    assert StylusLexer(1).tokenize(s)[0].value == ' '
    assert StylusLexer().tokenize(s + ' ')[0].value == ' '*9

    s = "X\tY"
    assert StylusLexer().tokenize(s)[2].type == 'WS'
    assert StylusLexer().tokenize(s)[2].value == ' '*8


def test_iter_token():
    s = "a"
    it = StylusLexer().yield_tokens(s)
    tok = next(it)
    assert tok.type == 'INDENT' and tok.value == ''
    tok = next(it)
    assert tok.type == 'NAME' and tok.value == 'a' and tok.line_position == 0
    tok = next(it)
    assert tok.type == 'EOL'
    tok = next(it)
    assert tok.type == 'STYLUS_END'

    with pytest.raises(StopIteration):
        next(it)

    # it = iter()


def test_indent():
    s = "  "
    assert StylusLexer().tokenize(s)[0].type == 'INDENT'
