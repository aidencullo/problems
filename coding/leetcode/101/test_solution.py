import pytest
from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3))),), True),
])
def test_solution(test_input, expected):
    result = Solution().isSymmetric(*test_input)
    assert result == expected
