from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        def helper(node, values):
            if len(values) == 1:
                print(1)
                return TreeNode(values[0])
            for i, value in enumerate(values):
                helper(None, values[:i] + values[i + 1:])
        helper(None, list(range(1, n + 1)))


"""
constraints

1 <= n <= 8

very small contraints
backtracking?
2^n algo?
n! even

i think this alg is n!

APPROACH
1. iterate over list of ints (in order)
2. for each int, create a node, then recurse on left and right subtree, with list to the right and left respectively

"""
