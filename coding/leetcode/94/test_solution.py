import pytest
from solution import Solution
from solution import TreeNode

@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(1, None, TreeNode(2, TreeNode(3))),), [1, 3, 2]),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.inorderTraversal(*test_input) == expected
