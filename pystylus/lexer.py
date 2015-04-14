#
#
#

from ply.lex import lex
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

        # pretend that the first character was a newline (helps with IDENT)
        self.prev_token_type = 'NEWLINE'

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

        t_itr = iter(self.lex.token, None)
        yield from t_itr

    def tokenize(self, string):
        """
        Tokenizes a string into a series of tokens. This uses yield_tokens to
        construct a list. It is recommended to use yield_tokens if iterating
        over all
        """
        return [t for t in self.yield_tokens(string)]
