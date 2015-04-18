#
# pystylus/parser.py
#

from ply.yacc import (yacc)
from pystylus.lexer import StylusLexer

# import pystylus.tokens as tokens
from pystylus.tokens import tokens as TOKENS


class StylusParser():
    """
    The stylus parser interprets a list of LexTokens as a complete stylus
    template. The parser keeps a list of blocks (self.stack), which have dict
    objects containing all information about the block.
    """

    def __init__(self):
        self.lexer = StylusLexer()
        self.tokens = TOKENS
        self.stack = []
        self.parser = yacc(module=self, start="stylus")

    def _push_scope(self):
        self._scope_stack.append(dict())

    def _pop_scope(self):
        self._scope_stack.pop()

    def parse(self, src, filename='', debuglevel=0):
        if not src:
            src = "\n"
        try:
            parse_tree = self.parser.parse(src, lexer=self.lexer, debug=2)
        except SyntaxError as err:
            assert hasattr(err, "lineno"), "SytaxError is missing lineno"
            raise
        return parse_tree

    def p_stylus(self, p):
        '''
            stylus  : block_list STYLUS_END
        '''
        self.stack = p[1]

    def p_block_list(self, p):
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

    def p_block(self, p):
        '''
            block : INDENT selector EOL
        '''
        print("BLOCK FOUND WITH SELECTOR:", p[2])
        p[0] = {
            'selector': p[2],
            'ident': len(p[1])
        }

    def p_simple_selector(self, p):
        '''
            selector : NAME
        '''
        p[0] = p[1]

    def p_ident_token(self, p):
        '''
            ident_token : NAME
        '''
        p[0] = p[1]

    def p_function_token(self, p):
        '''
            function_token : ident_token LPAREN
        '''
        p[0] = p[1] + p[2]


    def p_argument_list(self, p):
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
            p[0] = [p[1]] + p[-1]

    def p_at_keyword_token(self, p):
        '''
            at_keyword_token : STRUDEL ident_token
        '''
        p[0] = p[1] + p[2]

    def p_hash_token(self, p):
        '''
            hash_token : OCTOTHORPE ident_token
        '''
        p[0] = p[1] + p[2]

    def p_error(self, p):
        print("Syntax error at '%s'" % p.value)
