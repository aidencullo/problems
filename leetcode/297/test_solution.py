import pytest
from solution import Codec
from solution import TreeNode

@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(-1), None), None), TreeNode(7, TreeNode(2, TreeNode(9), None), None)),), None),
    ((TreeNode(1, TreeNode(2), TreeNode(3)),), None),
    ((TreeNode(1, None, TreeNode(2, TreeNode(3), None)),), None),
    ((None,), None),
])
def test_solution(test_input, expected):
    sol = Codec()
    deserialized_tree = sol.deserialize(sol.serialize(*test_input))
    assert compare_tree(deserialized_tree, *test_input)

def compare_tree(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.val != b.val:
        return False
    return compare_tree(a.left, b.left) and compare_tree(a.right, b.right)

def pretty_print(root):
    if root is None:
        return
    print(root.val)
    pretty_print(root.left)
    pretty_print(root.right)
