#
# tests/test_tokens.py
#

from ply import lex

from pystylus import tokens as TOKENS

class mock_stylus():
    def _normalize_whitespace(self, t):
        pass

def test_iter():
    l = [1,2,3,4]
    # i = iter(l.next, None)
    # for x in i:
        # x += 1
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
