#
# pystylus/parser.py
#

from ply.yacc import (yacc)

import pystylus.lexer
import pystylus.parsing_rules

from pystylus.errors import StylusParserError                            # noqa


class StylusParser:
    """
    The stylus parser interprets a list of LexTokens as a complete stylus
    template. This generates an abstract syntax tree out of components defined
    in pystylus.ast. The parser keeps a list of pystylus.ast.Block objects
    (self.stack), which contain all information about the string.

    This tree must be run through the... (interperter?) (yet to be implemented)
    to do the actual CSS generation.
    """

    def __init__(self):
        """
        Construct the parser. This sets up the initial lexer and parser
        objects.
        """
        self.lexer = pystylus.lexer.StylusLexer()
        self.stack = []
        self.parser = yacc(module=pystylus.parsing_rules, start="stylus")

    def parse(self, src, filename='', debuglevel=0):
        if not isinstance(src, str):
            raise TypeError
        if not src:
            src = "\n"
        try:
            parse_tree = self.parser.parse(src,
                                           lexer=self.lexer,
                                           debug=debuglevel
                                           )
        except SyntaxError as err:
            assert hasattr(err, "lineno"), "SytaxError is missing lineno"
            raise

        self.stack = parse_tree

        return parse_tree
