#
# pystylus/tokens.py
#

tokens = (
    'LONGARROW',
    'LONGWAVYARROW',
    'ARROW',
    'WAVYARROW',

    'LT',
    'GT',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'DOT',
    'OCTOTHORPE',
    'LPAREN',
    'RPAREN',

    'NEWLINE',
    'NUMBER',
    'NAME',
    'WS',
    'INDENT',
    'DEDENT',
    'ENDMARKER',
)
t_LONGARROW = r'-->'
t_LONGWAVYARROW = r'~~>'
t_ARROW = r'->'
t_WAVYARROW = r'~>'

t_NUMBER = r'\d+'
t_LT = r'<'
t_GT = r'>'

t_DOT = r'.'
t_OCTOTHORPE = r'\043'  # \043 == '#'

# t_INDENT = r'[ ]+'


def t_comment(t):
    r"[ ]*//[^\n]*"  # \043 is '#' ; otherwise PLY thinks it's an re comment
    pass


def t_WS(t):
    r" [ \t\f]+ "
    value = t.value.rsplit('\f', 1)[-1]
    # expand all tabs so they align with eight spaces
    while 1:
        pos = value.find('\t')
        if pos == -1:
            break
        filler = ' ' * (8 - (pos % 8))
        value = value[:pos] + filler + value[pos+1:]

    # if t.lexer.at_line_start and t.lexer.paren_count == 0:
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    t.type = "NEWLINE"
    # if t.lexer.paren_count == 0:
    return t


t_NAME = r"[a-zA-Z_][a-zA-Z0-9_]*"
# def t_NAME(self,t):
#   r"[a-zA-Z_][a-zA-Z0-9_]*"
#   return t


def t_INDENT(t):
    r'[ ]+'
    # raise Exception(dir(t))
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
