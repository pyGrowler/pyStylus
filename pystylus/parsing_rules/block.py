#
# pystylus/parsing_rules/block.py
#

#
# All block start with indent (may be len 0) and have a header-line, this
# *may* be followed by multiple indent lines.
#

def p_block(p):
    '''
        block : function_block
              | style_block
    '''
    p[0] = p[1]


def p_block_list(p):
    '''
        block_list : block block_list
                   | block
    '''
    # Handle the singular case
    if (len(p) == 2):
        print("BASE CASE: ", p[1])
        p[0] = [p[1]]
    # If multiple, add the first to the beginning of the list
    else:
        p[0] = [p[1]] + p[2]


def p_block_contents(p):
    '''
        block_contents : simple_statement EOL
                       | simple_statement EOL block_contents
    '''
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_empty_style_block(p):
    '''
        style_block : selector EOL
    '''
    p[0] = {
        'selector': p[1],
        'ident': 0,
        'contents': []
    }


def p_style_block(p):
    '''
        style_block : selector EOL INDENT block_contents DEDENT
    '''
    p[0] = {
        'selector': p[1],
        'ident': len(p[2])
    }


def p_header_line(p):
    '''
        header_line : NAME
    '''
    p[0] = p[1]


def p_simple_statement(p):
    '''
        simple_statement : NAME WS NAME
    '''
    p[0] = p[1]

def p_name_list(p):
    '''
        name_list : NAME
                  | NAME WS name_list
    '''
    p[0] = [p[1]] if len(p) == 2 else [p[1]] + p[3]
