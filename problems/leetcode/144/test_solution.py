import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(1, None, TreeNode(2, TreeNode(3), None)),), [1, 2, 3]),
])
def test_solution(test_input, expected):
    assert Solution().preorderTraversal(*test_input) == expected
