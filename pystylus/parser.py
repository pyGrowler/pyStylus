#
# pystylus/parser.py
#

from ply.yacc import (yacc)
from pystylus.lexer import StylusLexer

class StylusParser():

    def __init__(self):
        self.lexer = StylusLexer()

    def parse(self, str):

        for t in self.lexer.yield_tokens():
            pass
