import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]), TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))),),
        (([1], [1]), TreeNode(1),),
    ],
)
def test_solution(test_input, expected):
    assert compare_trees(Solution().constructFromPrePost(*test_input), expected)


def compare_trees(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    return (
        tree1.val == tree2.val
        and compare_trees(tree1.left, tree2.left)
        and compare_trees(tree1.right, tree2.right)
    )
