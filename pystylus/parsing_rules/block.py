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


def p_style_block(p):
    '''
        style_block : INDENT selector EOL
    '''
    p[0] = {
        'selector': p[2],
        'ident': len(p[1])
    }


def p_header_line(p):
    '''
        header_line : NAME
    '''
    p[0] = p[1]
