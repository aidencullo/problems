from solution import TreeNode, Solution


import pytest

def test_minimum_absolute_difference():
    # Test case 1
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(6)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)
    assert Solution().getMinimumDifference(root1) == 1

    # Test case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(48)
    root2.right.left = TreeNode(12)
    root2.right.right = TreeNode(49)
    assert Solution().getMinimumDifference(root2) == 1

    # Additional test case 1
    root3 = TreeNode(5)
    root3.left = TreeNode(4)
    root3.right = TreeNode(7)
    root3.right.left = TreeNode(6)
    assert Solution().getMinimumDifference(root3) == 1

    # Additional test case 2 (only two nodes)
    root4 = TreeNode(1)
    root4.right = TreeNode(3)
    assert Solution().getMinimumDifference(root4) == 2

    # Additional test case 3 (single node)
    root5 = TreeNode(1)
    assert Solution().getMinimumDifference(root5) == float('inf')


def test_minimum_absolute_difference_leet():
    # Test case 1
    root1 = TreeNode(236)
    root1.left = TreeNode(104)
    root1.right = TreeNode(701)
    root1.left.right = TreeNode(227)
    root1.right.right = TreeNode(911)
    assert Solution().getMinimumDifference(root1) == 9
