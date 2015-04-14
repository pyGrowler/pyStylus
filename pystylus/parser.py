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
            block : INDENT selector NEWLINE
                  | INDENT selector
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

    # State 5
    def p_error(self, p):
        print("Syntax error at '%s'" % p.value)
