import pytest
from solution import Solution
from solution import TreeNode

@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7))),), 5),
    ((TreeNode(2, TreeNode(2), TreeNode(2)),), -1),
    ((TreeNode(2, TreeNode(2), TreeNode(2, TreeNode(2), TreeNode(5))),), 5),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.findSecondMinimumValue(*test_input) == expected
