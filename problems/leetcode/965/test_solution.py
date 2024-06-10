import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(1, TreeNode(1, TreeNode(1), TreeNode(1)), TreeNode(1, right=TreeNode(1))),), True),
    ((TreeNode(2, TreeNode(2, TreeNode(5), TreeNode(2)), TreeNode(2)),), False),
])
def test_solution(test_input, expected):
    assert Solution().isUnivalTree(*test_input) == expected
