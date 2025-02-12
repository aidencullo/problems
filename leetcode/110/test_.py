import pytest

from solution import Solution
from util import TreeNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),), True),
        ((TreeNode(1, TreeNode(2), TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3))),), False),
        ((TreeNode(1, right=TreeNode(2, right=TreeNode(3))),), False),
    ],
)
def testSolution(test_input, expected):
    # Act
    result = Solution().isBalanced(*test_input)

    # Assert    
    assert result == expected
