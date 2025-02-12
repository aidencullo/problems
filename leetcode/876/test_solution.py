import pytest

from solution import Solution, TreeNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((TreeNode(1),), 0),
        ((TreeNode(1, TreeNode(1)),), 1),
        ((TreeNode(1, TreeNode(1), TreeNode(1)),), 2),
        ((TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)),), 3),
    ]
)
def testSolution(test_input, expected):
    assert Solution().diameterOfBinaryTree(*test_input) == expected
