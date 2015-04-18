#
# pystylus/parser.py
#

from ply.yacc import (yacc)
from pystylus.lexer import StylusLexer

# import pystylus.tokens as tokens
from pystylus.tokens import tokens as TOKENS

import pystylus.ast as AST

class StylusParser():
    """
    The stylus parser interprets a list of LexTokens as a complete stylus
    template. This generates an abstract syntax tree out of components defined
    in pystylus.ast. The parser keeps a list of pystylus.ast.Block objects
    (self.stack), which contain all information about the string.

    This tree must be run through the... (interperter?) (yet to be implemented)
    to do the actual CSS generation.
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
            parse_tree = self.parser.parse(src,
                                           lexer=self.lexer,
                                           debug=debuglevel
                                           )
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

    #
    # All block start with indent (may be len 0) and have a header-line, this
    # *may* be followed by multiple indent lines.
    #
    def p_block(self, p):
        '''
            block : function_block
                  | selector_block
        '''
        p[0] = p[1]

    def p_selector_block(self, p):
        '''
            selector_block : INDENT selector EOL
        '''
        p[0] = {
            'selector': p[2],
            'ident': len(p[1])
        }


    def p_function_block(self, p):
        '''
            function_block : INDENT function_def EOL
        '''
        p[0] = AST.Function(p[2]['name'], p[2]['args'], [])

    def p_header_line(self, p):
        '''
            header_line : NAME
        '''
        p[0] = p[1]


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

    def p_function_def(self, p):
        '''
            function_def : ident_token LPAREN RPAREN
                         | ident_token LPAREN WS RPAREN
        '''
        p[0] = {'name': p[1], 'args': []}

    def p_function_def_with_args_0(self, p):
        '''
            function_def : ident_token LPAREN argument_list RPAREN
                         | ident_token LPAREN argument_list WS RPAREN
        '''
        p[0] = {'name': p[1], 'args': p[3]}
        # p[0] = AST.Function(p[1], p[3], [])

    def p_function_def_with_args_1(self, p):
        '''
            function_def : ident_token LPAREN WS argument_list RPAREN
                         | ident_token LPAREN WS argument_list WS RPAREN
        '''
        p[0] = {'name': p[1], 'args': p[4]}
        # p[0] = AST.Function(p[1], p[4], [])


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
            p[0] = [p[1]] + p[len(p)-1]

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
        raise StylusParserError("Syntax error at '%s'" % p.value)


class StylusParserError(Exception):
    pass
