#
# pystylus/ast/comparison.py
#
"""
Comparison Node
"""


class ComparisonNode:
    """
    A comparison of two or more values. left is the first value in the
    comparison, ops the list of operators, and comparators the list of values
    after the first. If that sounds awkward, that’s because it is:
    """

    def __init__(self, name, ops, comparators):
        """
        A comparison of two or more values.
        """
        self.name = name
        self.ops = ops
        self.comparators = comparators


class EqualityOp:
    """
    Operator representing equality (==)
    """

    def __init__(self, left_expr, right_expr):
        self.left_side = left_expr
        self.right_side = right_expr


class LessThanOp:
    """
    Operator representing less than (<)
    """
    pass


class LessThanEqOp:
    """
    Operator representing less than (<)
    """
    pass


class GreaterThanOp:
    """
    Operator representing less than (>)
    """
    pass


class GreatorThanOp:
    """
    Operator representing less than (>)
    """
    pass
