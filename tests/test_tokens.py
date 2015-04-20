#
# tests/test_tokens.py
#

import pytest
from ply import lex
from pystylus import tokens as TOKENS


class mock_stylus():
    def _normalize_whitespace(self, t):
        pass


def test_iter():
    l = [1, 2, 3, 4]
    # i = iter(l.next, None)
    # for x in i:
    #     x += 1
    # raise Exception(l)


def test_zero():

    tokens = (
        'ZERO',
        'ONE',
        'TWO',
        'OTHER'
    )

    t_ZERO = r'0'
    t_ONE = r'1'

    def t_TWO(t):
        r'2'
        return t
        raise Exception(t.lexpos)

    s = "011002"
    lexer = lex.lex()
    lexer.input(s)
    count = 0
    for x in iter(lexer.token, None):
        count += 1
    assert len(s) == count


def test_token_0():

    lexer = lex.lex(module=TOKENS)
    lexer.input("9")
    tok = lexer.token()
    assert tok.type == 'NUMBER'
    assert tok.value == '9'
    # assert tok.value == '9.'
    return

    lexer.input("9.90")
    tok = lexer.token()
    assert tok.type == 'NUMBER'
    assert tok.value == '9.90'

    with pytest.raises(lex.LexError):
        lexer.input("9.90.")
        tok = lexer.token()
        assert tok.type == 'NUMBER'
        # raise Exception(tok)


def test_indent_token():

    t_NUMBER = r'[0-9]+(:?\.[0-9]*)'

    lexer = lex.lex(module=TOKENS)
    lexer.stylus = mock_stylus()
    lexer.input(" 5.2  ")

    tok = lexer.token()
    assert tok.type == "WS"
    tok = lexer.token()
    assert tok.type == "NUMBER"
    tok = lexer.token()
    assert tok.type == "WS"


def test_reserved():
    s = "if one"
    lexer = lex.lex(module=TOKENS)
    lexer.input(s)
    tok = lexer.token()
    assert tok.type == "IF"


def test_comment():
    s = "A// B C D\nE"
    lexer = lex.lex(module=TOKENS)
    lexer.input(s)
    tok = lexer.token()
    assert tok.type == "NAME" and tok.value == "A"
    tok = lexer.token()
    assert tok.type == "EOL"
    tok = lexer.token()
    assert tok.type == "NAME" and tok.value == "E" and tok.lineno == 2


def test_multiline_comment():
    s = "X/**/"
    lexer = lex.lex(module=TOKENS)
    lexer.input(s)
    tok = lexer.token()
    assert tok.type == "NAME" and tok.value == "X"
    tok = lexer.token()
    assert tok is None

    lexer.input("A /*\nthis is a comment*/B")
    tok = lexer.token()
    assert tok.type == "NAME" and tok.value == "A"
    tok = lexer.token()
    assert tok.type == "NAME" and tok.value == "B"
    tok = lexer.token()
    assert tok is None

    lexer.input("A/*\nthis is a comment B")
    tok = lexer.token()
    assert tok.type == "NAME" and tok.value == "A"
    with pytest.raises(Exception):
        tok = lexer.token()

def test_function_tokens():
    s = "foo()"
    lexer = lex.lex(module=TOKENS)
    lexer.input(s)
    tok = lexer.token()
    assert tok.type == "NAME" and tok.value == "foo"
    tok = lexer.token()
    assert tok.type == "LPAREN"
    tok = lexer.token()
    assert tok.type == "RPAREN"


def test_classname_token():
    s = ".html_class"
    lexer = lex.lex(module=TOKENS)
    lexer.input(s)
    tok = lexer.token()
    assert tok.type == "CLASSNAME" and tok.value == ".html_class"


def test_idname_token():
    s = "#an_id"
    lexer = lex.lex(module=TOKENS)
    lexer.input(s)
    tok = lexer.token()
    assert tok.type == "IDNAME" and tok.value == "#an_id"


def test_pseudoclass_token():
    s = ":first-child"
    lexer = lex.lex(module=TOKENS)
    lexer.input(s)
    tok = lexer.token()
    assert tok.type == "PSEUDOCLASS" and tok.value == ":first-child"
