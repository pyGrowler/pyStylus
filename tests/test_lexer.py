#
# tests/test_lexer.py
#

from pystylus.lexer import (StylusLexer, StylusLexerError)
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
    # NAME + WS + NAME + EOL + STYLUS_END
    assert len(StylusLexer().tokenize(s)) == 5


def test_tab_expansion():
    s = "\t"
    assert StylusLexer().tokenize(s)[0].type == 'INDENT'
    assert StylusLexer().tokenize(s)[0].value == ' '*8
    assert StylusLexer(1).tokenize(s)[0].value == ' '
    assert StylusLexer().tokenize(s + ' ')[0].value == ' '*9

    s = "X\tY"
    assert StylusLexer().tokenize(s)[1].type == 'WS'
    assert StylusLexer().tokenize(s)[1].value == ' '*8


def test_iter_token():
    s = "a"
    it = StylusLexer().yield_tokens(s)
    tok = next(it)
    assert tok.type == 'NAME' and tok.value == 'a' and tok.line_position == 0
    tok = next(it)
    assert tok.type == 'EOL'
    tok = next(it)
    assert tok.type == 'STYLUS_END'

    with pytest.raises(StopIteration):
        next(it)

    # it = iter()


def test_dedent():
    # INDENT NAME NEWLINE INDENT B NEWLINE DEDENT NAME
    s = "a\n b\nc"
    assert StylusLexer().tokenize(s)[5].type == 'DEDENT'


def test_bad_dedent():
    s = "a\n  b\n c"
    with pytest.raises(StylusLexerError):
        StylusLexer().tokenize(s)


def test_indent():
    s = "  "
    assert StylusLexer().tokenize(s)[0].type == 'INDENT'


def test_return():
    assert StylusLexer().tokenize("return")[0].type == 'RETURN'


def test_if():
    assert StylusLexer().tokenize("if x")[0].type == 'IF'


def test_function_tokens():
    toks = StylusLexer().tokenize("foo()")
    assert toks[0].type == "NAME" and toks[0].value == "foo"
    assert toks[1].type == "LPAREN"
    assert toks[2].type == "RPAREN"


def test_function_unicode():
    toks = StylusLexer().tokenize("π()\n return 3.141")
    assert toks[0].type == "NAME"
    assert toks[0].value == "π"
    assert toks[1].type == "LPAREN"
    assert toks[4].type == "INDENT"
    assert toks[5].type == "RETURN"
