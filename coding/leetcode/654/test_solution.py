import pytest
from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    (([3, 2, 1, 6, 0, 5],), TreeNode(6, TreeNode(3, None, TreeNode(2, None, TreeNode(1))), TreeNode(5, TreeNode(0)))),
])
def test_solution(test_input, expected):
    result = Solution().constructMaximumBinaryTree(*test_input)
    print_tree(result)
    assert compare_tree(Solution().constructMaximumBinaryTree(*test_input), expected)

def compare_tree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return compare_tree(t1.left, t2.left) and compare_tree(t1.right, t2.right)


def print_tree(t1):
    if not t1:
        return
    print(t1.val)
    print_tree(t1.left)
    print_tree(t1.right)
