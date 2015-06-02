#
# pystylus/parsing_rules/mathematical.py
#


def p_math_expression(p):
    '''
        math_expression : NUMBER
                        | NAME
                        | add_expression
                        | subtract_expression
                        | mult_expression
                        | division_expression
    '''
    p[0] = p[1]


def p_add_expression(p):
    '''
        add_expression : math_expression PLUS math_expression
    '''
    p[0] = p[1] + p[3]


def p_subtract_expression(p):
    '''
        subtract_expression : math_expression MINUS math_expression
    '''
    p[0] = p[1] - p[3]


def p_mult_expression(p):
    '''
        mult_expression : math_expression TIMES math_expression
                        | math_expression ASTERISK math_expression
    '''
    p[0] = p[1] * p[3]


def p_division_expression(p):
    '''
        division_expression : math_expression DIVIDE math_expression
                            | math_expression SLASH math_expression
    '''
    p[0] = p[1] / p[3]


def p_assignment_expression(p):
    '''
        assignment_expression : NAME EQUALS math_expression
    '''
    p[0] = {"output": p[0], "rhs": p[3]}
