import pytest

from solution import Solution, TreeNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((3,), [TreeNode(1, None, TreeNode(2, None, TreeNode(3))),
                TreeNode(1, None, TreeNode(3, TreeNode(2), None)),
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(3, TreeNode(1, None, TreeNode(2)), None),
                TreeNode(3, TreeNode(2, TreeNode(1), None), None)]),
    ],
)
def test_solution(test_input, expected):
    assert compare_trees(Solution().generateTrees(*test_input), expected)

def compare_trees(trees1, trees2):
    for t1, t2 in zip(trees1, trees2):
        if not compare_tree(t1, t2):
            return False
    return True
        
def compare_tree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    return t1.val == t2.val and compare_tree(t1.left, t2.left) and compare_tree(t1.right, t2.right)
