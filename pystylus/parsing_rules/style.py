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
        style_node : selector_list INDENT style_contents DEDENT
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


def p_selector_list(p):
    '''
        selector_list : selector EOL
                      | selector COMMA selector_list
                      | selector WS COMMA selector_list
                      | selector WS COMMA WS selector_list
                      | selector COMMA WS selector_list
                      | selector EOL selector_list
    '''
    p[0] = [p[1]] if len(p) <= 3 else [p[1]] + p[len(p)-1]


def p_selector(p):
    '''
        selector : NAME
                 | OCTOTHORPE NAME
                 | selector OCTOTHORPE NAME
                 | DOT NAME
                 | selector DOT NAME
    '''
    p[0] = p[1]
    if len(p) >= 3:
        p[0] += p[2],
    if len(p) == 4:
        p[0] += p[3]

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
