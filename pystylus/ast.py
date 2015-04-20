#
# pystylus/ast.py
#
"""
Elements of a pystylus abstract-syntax-tree
"""


class BaseElement:
    """
    Base class for all AST classes.
    """

    def __init__(self, token_list):
        self.tokens = token_list


class Block:
    """
    Block - starts with a heading line optionally followed by multiple lines
    """

    def __init__(self, header_line, statements):
        pass


class Function:

    def __init__(self, function_name, argument_list, content):
        self.name = function_name
        self.args = argument_list
        self.content = content
