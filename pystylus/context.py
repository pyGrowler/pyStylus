#
# pystylus/context.py
#
"""
Module for pystylus environment context
"""


class Context:
    """
    A class containing a requirements of a 'context' (environment) for running
    stylus logic. Contexts may be nested for scoped variables.
    """

    def __init__(self):
        """
        Create a context
        """
        self.vars = {}

    #
    # dict-accessors for variable names
    #

    def __getitem__(self, key):
        return self.vars[key]

    def __setitem__(self, key, value):
        # return self.vars.__setitem__(key, value)
        self.vars[key] = value
        return value

    def __getattr__(self, value):
        pass
