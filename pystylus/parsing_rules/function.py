#
# pystylus/parsing_rules/function.py
#

import pystylus.ast as AST


def p_node(p):
    '''
        node : function_node
    '''
    p[0] = p[1]


def p_function_node(p):
    '''
        function_node : function_def EOL INDENT function_contents DEDENT
    '''
    p[0] = AST.Function(p[1]['name'], p[1]['args'], p[4])


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


#
# argument_list is a comma separated list of names
#
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


def p_function_contents(p):
    '''
        function_contents : function_statement
                          | function_statement EOL function_contents
    '''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[3]


def p_function_statement(p):
    '''
        function_statement : return_statement
                           | math_expression
    '''
    p[0] = p[1]


def p_return_statement(p):
    '''
        return_statement : RETURN
                         | RETURN WS NAME
    '''
    p[0] = None if len(p) == 2 else p[3]


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


def p_assignment_expression(p):
    '''
        assignment_expression : NAME EQUALS math_expression
    '''
    p[0] = {"output": p[0], "rhs": p[3]}
