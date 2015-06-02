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


class ConditionalNode:
    """
    Node handling an if statement or if+elif+else chain of statements. The
    object is constructed from a 'conditional statement' and the node to be
    run if the conditional is later analyzed as True. An 'else' statement can
    be added by setting the optional else_node constructor argument. Additional
    else conditions to be checked before the final else condition may added by
    calling the add_elseif method. These will be checked in the order the
    method is called.
    """

    def __init__(self, condition, node, else_node=None):
        """
        Construct the node with a condition and the node to return if the
        condition is evaluated to be True. An optional 'else' node can be
        supplied which will be returned if the condition is False.
        """
        self.condition = condition
        self.node = node
        self.else_ifs = []
        if else_node is not None:
            self.set_else(else_node)

    def add_elif(self, condition, node):
        """
        Add an 'else if' condition to be checked in the event the 'if' returned
        False. These will be checked in the order supplied.
        """
        self.else_ifs.append((condition, node))

    def set_else(self, node):
        """
        Sets the 'else' condition of the conditional. This node is returned in
        the event that the 'if' and each 'elif' conditions return False.
        """
        self.else_node = node
