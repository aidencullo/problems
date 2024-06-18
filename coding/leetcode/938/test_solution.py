import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))), 7, 15), 32),
])
def test_solution(test_input, expected):
    assert Solution().rangeSumBST(*test_input) == expected
