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

from .nodes import *
from .identifiers import *
from .style import *
from .function import *

# from .block import *


def p_stylus(p):
    '''
        stylus  : node_list STYLUS_END
    '''
    p[0] = p[1]


def p_error(p):
    err_str = "Parsing error at %d:%d '%s'" % (
                                p.lineno,
                                p.line_position,
                                p.value)
    print(err_str)
    raise StylusParserError(err_str)
