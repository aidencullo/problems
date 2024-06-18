import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3)),), ["1->2->5", "1->3"]),
    ((TreeNode(1, None, None),), ["1"]),
    ((None,), []),
])
def test_solution(test_input, expected):
    assert Solution().binaryTreePaths(*test_input) == expected
