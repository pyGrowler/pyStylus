#
# pystylus/tokens.py
#

keyword_list = [
    'if',
    'for',
]

RESERVED = dict()

# copy keyword list into tokens and RESERVED
tokens = [
    RESERVED.__setitem__(name, name.upper()) or name.upper()
    for name in keyword_list
]

tokens += [

    'LONGARROW',
    'LONGWAVYARROW',

    'ARROW',
    'WAVYARROW',
    'DOUBLEARROW',

    'LT',
    'GT',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'DOT',
    'OCTOTHORPE',

    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',

    'NEWLINE',
    'NUMBER',
    'NAME',
    'WS',
    'INDENT',
    'DEDENT',
    'ENDMARKER',
    'EQUALS',
]

t_LONGARROW = r'-->'
t_LONGWAVYARROW = r'~~>'
t_ARROW = r'->'
t_WAVYARROW = r'~>'
t_DOUBLEARROW = r'=>'

t_NUMBER = r'(\d+(\.\d*)?|\.\d+)'
t_LT = r'<'
t_GT = r'>'

t_DOT = r'.'
t_OCTOTHORPE = r'\043'  # \043 == '#'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

t_EQUALS = r'='


def t_comment(t):
    r"[ ]*//[^\n]*"
    pass


def t_WS(t):
    r" [ \t\f]+ "
    t.lexer.stylus._normalize_whitespace(t)
    # if PREV_TOKEN_TYPE == 'NEWLINE':
    # t.type = 'INDENT'
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    t.type = "NEWLINE"
    # if t.lexer.paren_count == 0:
    return t


def t_NAME(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = RESERVED.get(t.value, "NAME")
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
