#
# pystylus/parsing_rules/style.py
#


def p_node(p):
    '''
        node : style_node
    '''
    p[0] = p[1]


def p_style_node(p):
    '''
        style_node : selector EOL INDENT style_contents DEDENT
    '''
    p[0] = p[1]


def p_style_contents(p):
    '''
        style_contents : style_statement EOL
                       | style_statement EOL style_contents
    '''
    p[0] = [p[1]] if len(p) == 3 else [p[1]] + p[3]


def p_style_statement(p):
    '''
        style_statement : NAME WS name_list
                        | NAME COLON WS name_list
                        | NAME WS COLON WS name_list
    '''
    p[0] = [p[1], p[len(p)-1]]


def p_id_selector(p):
    '''
        selector : NAME
                 | CLASSNAME
                 | IDNAME
                 | selector NAME
                 | selector CLASSNAME
                 | selector IDNAME
    '''
    p[0] = p[1]
    if len(p) == 3:
        p[0] += p[2]


def p_name_list(p):
    '''
        name_list : NAME
                  | style_number
                  | NAME WS name_list
                  | style_number WS name_list
    '''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[3]


def p_style_number(p):
    '''
        style_number : SUFFIXED_NUMBER
                     | NUMBER
    '''
    p[0] = str(p[1])


# def p_class_selector(p):
#     '''
#         selector : DOT NAME
#                  | selector DOT NAME
#     '''
#     p[0] = ''.join(p)
