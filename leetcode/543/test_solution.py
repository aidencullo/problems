import pytest

from solution import Solution
from solution import TreeNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)), ), 3),
    ]
)
def testSolution(test_input, expected):
    s = Solution()
    assert s.diameterOfBinaryTree(*test_input) == expected
    
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
