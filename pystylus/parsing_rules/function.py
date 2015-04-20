#
# pystylus/parsing_rules/function.py
#

import pystylus.ast as AST


def p_function_block(p):
    '''
        function_block : INDENT function_def EOL block_contents
    '''
    p[0] = AST.Function(p[2]['name'], p[2]['args'], [])


def p_function_def(p):
    '''
        function_def : ident_token LPAREN RPAREN
                     | ident_token LPAREN WS RPAREN
    '''
    p[0] = {'name': p[1], 'args': []}


def p_function_def_with_args_0(p):
    '''
        function_def : ident_token LPAREN argument_list RPAREN
                     | ident_token LPAREN argument_list WS RPAREN
    '''
    p[0] = {'name': p[1], 'args': p[3]}
    # p[0] = AST.Function(p[1], p[3], [])


def p_function_def_with_args_1(p):
    '''
        function_def : ident_token LPAREN WS argument_list RPAREN
                     | ident_token LPAREN WS argument_list WS RPAREN
    '''
    p[0] = {'name': p[1], 'args': p[4]}
    # p[0] = AST.Function(p[1], p[4], [])


def p_argument_list(p):
    '''
        argument_list : NAME
                      | NAME COMMA argument_list
                      | NAME WS COMMA argument_list
                      | NAME COMMA WS argument_list
                      | NAME WS COMMA WS argument_list
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[len(p)-1]

def p_return_statement(p):
    '''
        return_statement : RETURN NAME
    '''
    p[0] = p[2]


def p_math_expression(p):
    '''
        math_expression : add_expression
                        | subtract_expression
    '''
    p[0] = p[1]

def p_add_expression(p):
    '''
        add_expression : math_expression PLUS math_expression
    '''
    p[0] = p[1] + p[2]

def p_subtract_expression(p):
    '''
        subtract_expression : math_expression MINUS math_expression
    '''
    p[0] = p[1] + p[2]
