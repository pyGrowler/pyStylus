#
# pystylus/ast/conditional.py
#
"""
Contains the ConditionalNode element of the pystylus AST - handling if
statements
"""


class ConditionalNode:
    """
    Node handling an if statement or if+elif+else chain of statements. The
    object is constructed from a 'conditional statement' and the node to be run
    if the conditional is later analyzed as True. An 'else' statement can be
    added by setting the optional else_node constructor argument. Additional
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
