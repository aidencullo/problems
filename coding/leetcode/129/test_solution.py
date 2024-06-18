import pytest

from solution import Solution
from solution import TreeNode

@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(1, TreeNode(2), TreeNode(3))), 25),
    ((TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))), 1026),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.sumNumbers(test_input) == expected
