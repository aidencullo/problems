import pytest

from solution import Solution
from solution import TreeNode

@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(2, TreeNode(1), TreeNode(3)),), True),
    ((TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))),), False),
    ((TreeNode(1, TreeNode(1), TreeNode(1)),), False),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.isValidBST(*test_input) == expected
