#
# tests/test_lexer.py
#

from pystylus.lexer import StylusLexer


def test_construction():
    lexer = StylusLexer()
    assert lexer


def test_line():
    s = """This is a simple line"""
    lexer = StylusLexer()
    tokens = lexer.tokenize(s)
    for x in tokens[1:]:
        if x.type == 'WS':
            assert x.value == ' '
        assert x.type in ('NAME','WS')


def test_comment():
    s = """This has   // a comment"""
    assert len(StylusLexer().tokenize(s)) == 4


def test_tab_expansion():
    s = "\t"
    assert StylusLexer().tokenize(s)[0].type == 'INDENT'
    assert StylusLexer().tokenize(s)[0].value == ' '*8
    assert StylusLexer(1).tokenize(s)[0].value == ' '
    assert StylusLexer().tokenize(s + ' ')[0].value == ' '*9


def test_iter_token():
    s = "\t"

    # it = iter()

def test_ident():
    s = "  "
