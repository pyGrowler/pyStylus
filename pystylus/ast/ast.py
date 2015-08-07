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


class FunctionNode:
    """
    A callable function
    """
    def __init__(self, function_name, argument_list, content):
        self.name = function_name
        self.args = argument_list
        self.content = content


class StyleNode:
    """
    The core of the stylus language. A StyleNode contains the css selectors and
    the style rules pertaining to those selectors. It also has a list of nested
    StyleNodes. When rendered to string, objects output the CSS representation
    of the styles.
    """

    def __init__(self, selectors, contents):
        """
        Construct a StyleNode with a list of selectors and the contents of the
        style block.
        """
        if any([selector.startswith('-') for selector in selectors]):
            raise Exception("DashedSelector")
        self.selectors = selectors
        self.contents = [rule[0] + ':' + ' '.join(rule[1])
                         for rule in contents['rules']]

    def __str__(self):
        """
        Convert the StyleNode to a string by printing CSS.
        """
        # print('C', self.contents)
        s = ', '.join(self.selectors)
        s += '{' + ';'.join(self.contents) + '}'
        return s
