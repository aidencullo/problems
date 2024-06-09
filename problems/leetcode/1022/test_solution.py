import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(1, TreeNode(0, TreeNode(0), TreeNode(1)), TreeNode(1, TreeNode(0), TreeNode(1))),), 22),
])
def test_solution(test_input, expected):
    assert Solution().sumRootToLeaf(*test_input) == expected
