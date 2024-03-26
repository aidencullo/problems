import pytest

from solution import Solution
from solution import TreeNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([3,9,10,11,20,15,7], [10,9,11,3,15,20,7]), TreeNode(3, TreeNode(9, TreeNode(10), TreeNode(11)), TreeNode(20, TreeNode(15), TreeNode(7)))),
        (([3,9,20,15,7], [9,3,15,20,7]), TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))),
        (([1,2], [2,1]), TreeNode(1, TreeNode(2), None)),
    ]
)
def testSolution(test_input, expected):
    actual = Solution().buildTree(*test_input)
    compare_trees(actual, expected)

def compare_arrays(a, b):
    assert len(a) == len(b)
    for i in range(len(a)):
        assert a[i] == b[i]

def compare_trees(a, b):
    assert (a is None) == (b is None)
    if a is None:
        return
    assert a.val == b.val
    compare_trees(a.left, b.left)
    compare_trees(a.right, b.right)
