#
# pystylus/parsing_rules/logical.py
#


def p_equals_expression(p):
    '''
        equals_expression : math_expression EQUALS EQUALS math_expression
    '''
    p[0] = p[1]


def p_not_equals_expression(p):
    '''
        not_equals_expression : math_expression BANG EQUALS math_expression
                              | math_expression NEQUALS math_expression
    '''
    p[0] = p[1]


def p_less_than_expression(p):
    '''
        less_than_expression : math_expression LT math_expression
    '''
    p[0] = p[1] < p[3]


def p_greater_than_expression(p):
    '''
        greater_than_expression : math_expression GT math_expression
    '''
    p[0] = p[1] > p[3]


def p_conditional(p):
    '''
        conditional : NAME
                    | less_than_expression
                    | greater_than_expression
                    | equals_expression
                    | not_equals_expression
    '''
    p[0] = p[1]


def p_conditional_in_parens(p):
    '''
        conditional : LPAREN conditional RPAREN
    '''
    p[0] = p[2]
