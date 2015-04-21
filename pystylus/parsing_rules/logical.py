#
# pystylus/parsing_rules/logical.py
#


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
