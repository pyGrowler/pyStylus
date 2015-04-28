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
        if_node : IF WS conditional EOL INDENT node DEDENT
    '''
    p[0] = AST.ConditionalNode(p[2], p[5])


def p_if_else_node(p):
    '''
        if_node : IF conditional EOL INDENT node DEDENT else_node
    '''
    p[0] = AST.ConditionalNode(p[2], p[5], p[7])


def p_if_elif_nodes(p):
    '''
        if_node : IF conditional EOL INDENT node DEDENT else_if_list
    '''
    p[0] = AST.ConditionalNode(p[2], p[5])

    for condition, node in p[7]:
        p[0].add_elif(condition, node)


def p_if_elif_else_nodes(p):
    '''
        if_node : IF conditional EOL INDENT node DEDENT else_if_list else_node
    '''
    p[0] = AST.ConditionalNode(p[2], p[5], p[7])
    for condition, node in p[7]:
        p[0].add_elif(condition, node)


def p_else_if_list(p):
    '''
        else_if_list : ELIF conditional INDENT node DEDENT
                     | else_if_list ELIF conditional INDENT node DEDENT
    '''
    if len(p) == 6:
        p[0] = [(p[2], p[4])]
    else:
        p[0] = p[1] + [(p[3], p[5])]


def p_long_else_if_list(p):
    '''
        else_if_list : ELSE IF conditional INDENT node DEDENT
                     | else_if_list ELSE IF conditional INDENT node DEDENT
    '''
    if len(p) == 7:
        p[0] = [(p[3], p[5])]
    else:
        p[0] = p[1] + [(p[4], p[6])]


def p_else_node(p):
    '''
        else_node : ELSE EOL INDENT node DEDENT
    '''
    p[0] = p[4]
