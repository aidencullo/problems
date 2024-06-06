import pytest

from solution import Solution, TreeNode


def test_solution():

    tree = TreeNode(7,
                    TreeNode(4),
                    TreeNode(3,
                                TreeNode(6),
                                TreeNode(19)))
    target = tree.right
    assert Solution().getTargetCopy(tree, tree, target) == target
