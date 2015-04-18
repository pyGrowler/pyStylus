#
# pystylus/parsing_rules/__init__.py
#
"""
Sub-module to keep parsing rules organized.

This should only be used by the pystylus.parser.Parser class to do the parsing.
"""

# Let PLY be aware of the tokens
from pystylus.tokens import tokens
import pystylus.ast as AST
from pystylus.errors import StylusParserError

from .identifiers import *
from .function import *


def p_stylus(p):
    '''
        stylus  : block_list STYLUS_END
    '''
    p[0] = p[1]


def p_block_list(p):
    '''
        block_list : block block_list
                   | block
    '''
    # Handle the singular case
    if (len(p) == 2):
        print("BASE CASE: ", p[1])
        p[0] = [p[1]]
    # If multiple, add the first to the beginning of the list
    else:
        p[0] = [p[1]] + p[2]


#
# All block start with indent (may be len 0) and have a header-line, this
# *may* be followed by multiple indent lines.
#
def p_block(p):
    '''
        block : function_block
              | style_block
    '''
    p[0] = p[1]


def p_style_block(p):
    '''
        style_block : INDENT selector EOL
    '''
    p[0] = {
        'selector': p[2],
        'ident': len(p[1])
    }


def p_header_line(p):
    '''
        header_line : NAME
    '''
    p[0] = p[1]


def p_simple_selector(p):
    '''
        selector : NAME
    '''
    p[0] = p[1]


def p_math_expression(p):
    '''
        math_expression : NAME WS PLUS WS NAME EOL
    '''
    p[0] = p[1] + p[3]


def p_error(p):
    err_str = "Syntax error at %d:%d '%s'" % (
                                p.lineno,
                                p.line_position,
                                p.value)
    print(err_str)
    raise StylusParserError(err_str)