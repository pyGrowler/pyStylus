#
# pystylus/parser.py
#

from ply.yacc import (yacc)
from pystylus.lexer import StylusLexer

import pystylus.tokens

class StylusParser():

    def __init__(self):
        self.lexer = StylusLexer()
        self.tokens = pystylus.tokens.tokens
        self.stack = [{}]
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
        """
            stylus  : INDENT block STYLUS_END
        """
        p[0] = p[1]

    def p_statement_assign(self, p):
        'statement : NAME EQUALS expression'
        names[t[1]] = p[3]

    def p_statement_expression(self, p):
        'expression : '
        pass

    def p_statement_block(self, p):
        'block : INDENT NAME INDENT'
        pass

    def p_error(self, p):
        print("Syntax error at '%s'" % p.value)
