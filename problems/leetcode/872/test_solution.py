import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))), TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),), True),
    ((TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)),), True),
    ((TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))),), False),
    ((TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))),), False),
    ((TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))),), False),
])
def test_solution(test_input, expected):
    assert Solution().leafSimilar(*test_input) == expected
