import pytest

from solution import Solution
from solution import TreeNode

@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))), True),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.isSameTree(*test_input) == expected
