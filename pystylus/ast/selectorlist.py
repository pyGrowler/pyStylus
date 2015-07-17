#
# pystylus/ast/selectorlist.py
#
"""
Defines the SelectorList node type in the pystylus AST
"""


class SelectorList:
    """
    The selector list is a list of valid CSS selectors. This is found at the
    beginning of a Style Block
    """

    def __init__(self, *selectors):
        self.selectors = selectors
