#
#
#

from ply.lex import lex
from . import tokens


class StylusLexer:

    def __init__(self):

        self.lex = lex(module=tokens)

    def _annotate_(self):
        pass
