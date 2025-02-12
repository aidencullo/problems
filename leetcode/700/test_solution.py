import pytest

from solution import Solution
from solution import TreeNode

@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 2), TreeNode(2, TreeNode(1), TreeNode(3))),
    ((TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7)), 5), None),
])
def test_solution(test_input, expected):
    s = Solution()
    assert compare_trees(s.searchBST(*test_input), expected)

def compare_trees(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    if tree1.val != tree2.val:
        return False
    return compare_trees(tree1.left, tree2.left) and compare_trees(tree1.right, tree2.right)
