#
# pystylus/parsing_rules/comparison.py
#

from pystylus.ast.comparison import (
    EqualityOp
)


def p_equals_expression(p):
    '''
        equals_expression : expression EQUALS EQUALS expression
    '''
    p[0] = EqualityOp(p[1], p[4])
