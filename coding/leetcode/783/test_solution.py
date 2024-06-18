import pytest
from solution import Solution
from solution import TreeNode

@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7))),), 1),
    ((TreeNode(1, None, TreeNode(2)),), 1),
    ((TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49))),), 1),
    ((TreeNode(90, TreeNode(69, TreeNode(49), TreeNode(89)), TreeNode(52)),), 1),
])
def test_solution(test_input, expected):
    assert Solution().minDiffInBST(*test_input) == expected
