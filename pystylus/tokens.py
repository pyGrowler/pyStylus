#
# pystylus/tokens.py
#

keyword_list = [
    'if',
    'else',
    'for',
    'return',
    'import',
]

RESERVED = dict()

# copy keyword list into tokens and RESERVED
tokens = [
    RESERVED.__setitem__(name, name.upper()) or name.upper()
    for name in keyword_list
]

tokens += [

    'LT',
    'GT',

    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',

    'COMMA',
    'DOT',
    'ASTERISK',
    'AMPERSAND',
    'OCTOTHORPE',
    'COLON',
    'TILDE',

    'SLASH',
    'STRUDEL',

    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',

    'SUFFIXED_NUMBER',
    'NUMBER',
    'NAME',
    'ESCAPE',
    'WS',
    'INDENT',
    'DEDENT',

    'EOL',         # End of line
    'STYLUS_END',  # End of stylus content (file or string)
]

t_LT = r'<'
t_GT = r'>'

t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'×'
t_DIVIDE = r'÷'

t_EQUALS = r'='

t_COMMA = r','
t_DOT = r'\.'
t_ASTERISK = r'\*'
t_AMPERSAND = r'&'
t_OCTOTHORPE = r'\043'  # \043 == '#'
t_COLON = r':'
t_TILDE = r'~'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

t_SLASH = r'/'
# t_BSLASH = r'\\'
t_STRUDEL = r'@'

t_SUFFIXED_NUMBER = r'(\d+(\.\d*)?|\.\d+)([a-zA-Z]+|%)'
t_NUMBER = r'(\d+(\.\d*)?|\.\d+)'

t_ESCAPE = r'\\([0-9a-fA-F]{1,6}\w?|[^0-9a-fA-F\n])'

def t_comment(t):
    r"[ ]*//[^\n]*"
    pass


def t_multiline_comment(t):
    r"[ ]*/\*([^\*]|\*[^/])*\*/"
    pass


def t_unterminated_multiline_comment(t):
    r"[ ]*/\*([^\*]|\*[^/])*"
    e_str = "Unterminated multi-line comment starting at line %d" % (t.lineno)
    raise Exception(e_str)


def t_WS(t):
    r" [ \t\f]+ "
    t.lexer.stylus._normalize_whitespace(t)
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    t.type = "EOL"
    return t


def t_NAME(t):
    r'(?u)[^\W0-9]\w*'
    # r"\-?[a-zA-Z_-][a-zA-Z0-9_-]*"
    t.type = RESERVED.get(t.value, "NAME")
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
