#
# pystylus/lexer.py
#

from ply.lex import (lex, LexToken)

from pystylus.errors import StylusLexerError
from . import tokens


class StylusLexer:
    """
    A class which encapsulates a ply.lex object and loads the pystylus tokens
    automatically. This modifies the default behavior of the lex class by
    iterating over all tokens and marking indentations (INDENT/DEDENT) before
    being sent to the parser (or any user's code).
    """

    def __init__(self, tab_expansion=8):
        """
        Constructs the lexer by creating a ply.lex.lex instance with the
        pystylus.tokens as the module parameter.
        """
        self.lex = lex(module=tokens)
        self.lex.stylus = self
        self.tab_expansion = tab_expansion

        # pretend that the first character was a newline (helps with INDENT)
        self.prev_token_type = 'EOL'

    def _normalize_whitespace(self, token):
        """
        Method called upon finding a whitespace token. This finds any tab
        ('\t') characters and expands them into spaces. This uses the object's
        tab_expansion parameter to align the tabs to a fixed number of spaces.
        The default is the POSIX standard, 8.
        """
        assert isinstance(token.value, str)
        pos = token.value.find('\t')
        while pos != -1:
            filler = ' ' * (self.tab_expansion - (pos % self.tab_expansion))
            token.value = token.value[:pos] + filler + token.value[pos+1:]
            pos = token.value.find('\t')

    def _gen_token(self, type, value='', lnum=None, position=0, lexpos=None):
        tok = LexToken()
        tok.lexer = self.lex
        tok.type = type
        tok.value = value
        tok.line_position = position
        # I think this will work...
        tok.lineno = self.lex.lineno if lnum is None else lnum
        tok.lexpos = self.lex.lexpos if lexpos is None else lexpos
        return tok

    def _empty_ident(self):
        return self._gen_token('INDENT')

    @classmethod
    def _determine_indents(cls, token_iter):
        """
        Method called upon tokenizing a string. This loops through and changes
        any whitespace tokens that follow a newline into an INDENT or DEDENT
        token.
        This modifies the tokens in-place.
        """
        pass

    def yield_tokens(self, string):
        """
        A generator which tokenizes a string into a series of pystylus tokens.
        """
        self.lex.input(string)
        indent_stack = []  # stack of indent lengths
        line_position = 0
        for t in iter(self.lex.token, None):
            if line_position is 0:
                # if starting a line without whitespace
                if t.type != 'WS':
                    # dedent all indents
                    while len(indent_stack) > 0:
                        val = indent_stack.pop()
                        yield self._gen_token('DEDENT', value=val)
                    # return empty indent
                    yield self._empty_ident()

                # if nothing on the indent_stack - this must be an indent
                elif len(indent_stack) is 0:
                    t.type = 'INDENT'
                    indent_stack.append(len(t.value))

                # We have read in whitespace, determine if in- or de- dent
                else:
                    # if shorter than previous indent, this must be a dedent
                    if len(t.value) < indent_stack[-1]:
                        # loop through indents, finding one that matches
                        while len(indent_stack):
                            # if in-between
                            if len(t.value) == indent_stack[-1]:
                                t.type = 'DEDENT'
                                break

                            elif len(t.value) > indent_stack[-1]:
                                raise StylusLexerError("Misaligned DEDENT")

                            # remove last element
                            indent_stack.pop()

                        # len(indent_stack)
                        if len(indent_stack) == 0:
                            raise StylusLexerError("Misaligned DEDENT")

                    else:
                        # if not shorter, this is an indent
                        t.type = 'INDENT'

                        # if LONGER, push length to stack
                        if len(t.value) > indent_stack[-1]:
                            indent_stack.append(len(t.value))

            t.line_position = line_position
            line_position = 0 \
                if t.type is 'EOL' \
                else line_position + len(t.value)
            prev_type = t.type
            yield t

        # Always finish the file with a newline, even if not there...
        if line_position != 0:
            yield self._gen_token('EOL')
        yield self._gen_token('STYLUS_END')

    def tokenize(self, string):
        """
        Tokenizes a string into a series of tokens. This uses yield_tokens to
        construct a list. It is recommended to use yield_tokens if iterating
        over all
        """
        return [t for t in self.yield_tokens(string)]

    def input(self, string):
        self.token_iterator = self.yield_tokens(string)

    def token(self):
        try:
            return next(self.token_iterator)
        except StopIteration:
            return None
