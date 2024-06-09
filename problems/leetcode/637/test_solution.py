import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),), [3.00000, 14.50000, 11.00000]),
])
def test_solution(test_input, expected):
    assert Solution().averageOfLevels(*test_input) == expected
