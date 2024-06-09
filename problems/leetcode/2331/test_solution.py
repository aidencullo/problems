import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(2, TreeNode(1), TreeNode(3, TreeNode(0), TreeNode(1))),), True),
])
def test_solution(test_input, expected):
    assert Solution().evaluateTree(*test_input) == expected
