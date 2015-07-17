#
# tests/test_tokens.py
#

import pytest
from ply import lex
from pystylus import tokens as TOKENS

from re import UNICODE

@pytest.fixture
def lexer():
    lexer = lex.lex(module=TOKENS)
    lexer.stylus = mock_stylus()
    return lexer

class mock_stylus():
    def _normalize_whitespace(self, t):
        pass


def iter_lexer(lex):
    next_token = lex.token()
    while next_token is not None:
        yield next_token
        next_token = lex.token()
    raise StopIteration


def test_token_0(lexer):
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


@pytest.mark.parametrize("string, token_type", [
    ("Andrew", "NAME"),
    ("@import", "IMPORT"),
    ("import", "NAME"),
    ("if", "IF"),
    ("@", "STRUDEL"),
    ("(", "LPAREN"),
    (")", "RPAREN"),
    ("7", "NUMBER"),
    ("9.123", "NUMBER"),
    ("9.123E-4", "SUFFIXED_NUMBER"),
])
def test_token_type(lexer, string, token_type):
    lexer.input(string)
    token = lexer.token()
    assert token.type == token_type


@pytest.mark.parametrize("string", [
    "Andrew",
    'lowercase',
    'UPPERCASE',
])
def test_token_values(lexer, string):
    lexer.input(string)
    token = lexer.token()
    assert token.type == 'NAME'
    assert token.value == string


@pytest.mark.parametrize("string, token_types", [
    ("python is cool", ["NAME", "WS"] * 3),
    ("if something @import", ["IF", "WS", "NAME", "WS", "IMPORT"]),
    ("if elif else", "IF WS ELIF WS ELSE".split())
])
def test_token_types(lexer, string, token_types):
    lexer.input(string)
    for token, token_type in zip(iter_lexer(lexer), token_types):
        assert token.type == token_type

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


def test_multiline_comment(lexer):
    s = "X/**/"
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


def test_unicode_token():
    s = "πpy"
    lexer = lex.lex(module=TOKENS, reflags=UNICODE)
    lexer.input(s)
    tok = lexer.token()
    assert tok.type == "NAME" and tok.value == "πpy"