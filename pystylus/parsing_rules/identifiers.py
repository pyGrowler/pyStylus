#
# pystylus/parsing_rules/identifiers.py
#
"""
Parsing rules for different identifiers
"""


def p_at_keyword_token(p):
    '''
        at_keyword_token : STRUDEL ident_token
    '''
    p[0] = p[1] + p[2]


def p_hash_token(p):
    '''
        hash_token : OCTOTHORPE ident_token
    '''
    p[0] = p[1] + p[2]


def p_ident_token(p):
    '''
        ident_token : NAME
    '''
    p[0] = p[1]
