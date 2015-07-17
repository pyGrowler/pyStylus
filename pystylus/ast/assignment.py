#
# pystylus/ast/assignment.py
#
"""
Defines the AST AssignmentNode
"""


class AssignmentNode:
    """
    Used anywhere an assignment to a variable happens in the stylus file.
    """

    def __init__(self, names, rhs):
        self.names = names
        self.rhs = rhs
