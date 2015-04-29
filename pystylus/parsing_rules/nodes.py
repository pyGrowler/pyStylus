#
# pystylus/parsing_rules/nodes.py
#

import pystylus.ast as AST


def p_node_list(p):
    '''
        node_list : node node_list
                  | node
    '''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[2]


def p_nodes_node(p):
    '''
        node : import_node
             | assignment_node
             | if_node
    '''
    p[0] = p[1]


def p_import_node(p):
    '''
        import_node : IMPORT NAME
    '''
    p[0] = p[1]


def p_assignment_node(p):
    '''
        assignment_node : NAME EQUALS name_list
    '''
    p[0] = {"output": p[0], "rhs": p[3]}


def p_for_loop_node(p):
    '''
        for_loop : FOR conditional EOL INDENT node DEDENT
    '''
    p[0] = p[2]


def p_if_node(p):
    '''
        if_node : if_statement
    '''
    p[0] = AST.ConditionalNode(p[1]['condition'], p[1]['node'])


def p_if_else_node(p):
    '''
        if_node : if_statement else_statement
    '''
    condition, node = p[1].values()
    p[0] = AST.ConditionalNode(condition, node, p[2])


def p_if_elif_nodes(p):
    '''
        if_node : if_statement elif_list
    '''
    p[0] = AST.ConditionalNode(p[1]['condition'], p[1]['node'])

    for elif_statement in p[2]:
        condition, node = elif_statement.values()
        p[0].add_elif(condition, node)


def p_if_elif_else_nodes(p):
    '''
        if_node : if_statement elif_list else_statement
    '''
    condition, node = p[1].values()
    p[0] = AST.ConditionalNode(condition, node, p[3])
    for elif_statement in p[2]:
        condition, node = elif_statement.values()
        p[0].add_elif(condition, node)


def p_if_statement(p):
    '''
        if_statement : IF conditional EOL INDENT node DEDENT
                     | IF WS conditional EOL INDENT node DEDENT
    '''
    l = len(p)
    p[0] = {
        "condition": p[l-5],
        "node": p[l-2]
    }


def p_elif_statement(p):
    '''
        elif_statement : ELIF conditional EOL INDENT node DEDENT
                       | ELIF WS conditional EOL INDENT node DEDENT
                       | ELSE IF conditional EOL INDENT node DEDENT
                       | ELSE IF WS conditional EOL INDENT node DEDENT
    '''
    l = len(p)
    p[0] = {
        "condition": p[l-5],
        "node": p[l-2]
    }


def p_else_statement(p):
    '''
        else_statement : ELSE EOL INDENT node DEDENT
    '''
    p[0] = p[4]


def p_elif_list(p):
    '''
        elif_list : elif_statement
                  | elif_list elif_statement
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]
