import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), None)),), 6),
    ((TreeNode(1, None, None),), 1),
    ((None,), 0),
])
def test_solution(test_input, expected):
    assert Solution().countNodes(*test_input) == expected
