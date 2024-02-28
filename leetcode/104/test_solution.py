import pytest

from solution import Solution, TreeNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),), 3),
    ]
)
def testSolution(test_input, expected):
    assert Solution().maxDepth(*test_input) == expected
