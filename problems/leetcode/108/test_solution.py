import pytest
from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    (([-10,-3,0,5,9],), TreeNode(0, TreeNode(-3, TreeNode(-10), None), TreeNode(9, TreeNode(5), None))),
])
def test_solution(test_input, expected):
    result = Solution().sortedArrayToBST(*test_input)
    assert compare_tree(result, expected)


def compare_tree(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and compare_tree(a.left, b.left) and compare_tree(a.right, b.right)
