#
# pystylus/parsing_rules/nodes.py
#


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
        if_node : IF conditional EOL INDENT node DEDENT
    '''
    p[0] = p[2]


def p_if_else_node(p):
    '''
        if_node : IF conditional EOL INDENT node DEDENT ELSE INDENT node DEDENT
    '''
    p[0] = p[2]
