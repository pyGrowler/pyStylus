#
# tests/test_tokens.py
#

from ply import lex

from pystylus import tokens as TOKENS


def test_zero():

    tokens = (
       'ONE',
       'RPAREN'
    )

    t_ONE = r'1'

    # def t_ONE

    lexer = lex.lex()
    lexer.input("0123")
    tok = lexer.token()
    print(tok)


def test_token_0():

    lexer = lex.lex(module=TOKENS)
    return
    lexer.input("9")
    tok = lexer.token()
    assert tok.type == 'NUMBER'
    assert tok.value == '9'
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
    lexer.input(" 5.2  ")

    tok = lexer.token()
    assert tok.type == "WS"
    assert lexer.token().type == "NUMBER"
    assert tok.type == "WS"
