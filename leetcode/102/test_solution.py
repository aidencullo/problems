# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))), [[3],[9,20],[15,7]]),
        (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5), None)), None), None), [[1],[2], [3],[4],[5]]),
    ]
)
def testSolution(test_input, expected):
    assert Solution().levelOrder(test_input) == expected
