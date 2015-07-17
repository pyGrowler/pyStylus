#
# pystylus/ast/importnode.py
#
"""
Contains the two import nodes in the stylus AST
"""


class ImportNode:
    """
    A stylus import statement created from the line "@import xxx" where the xxx
    does NOT end with ".css". This is a command to stylus to import another
    file into the current one.
    """

    def __init__(self, name):
        self.name = name


class LiteralImportNode:
    """
    A 'literal' @import statement that will be rendered as-is into the css
    output. This is created if the stylus line has the form "@import xxx.css".
    """

    def __init__(self, name):
        self.name = name
