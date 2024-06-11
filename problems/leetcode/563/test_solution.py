from solution import Solution, TreeNode


def test_find_tilt():
    solution = Solution()

    # Test case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    assert solution.findTilt(root1) == 1

    # Test case 2
    root2 = TreeNode(4)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(5)
    root2.right = TreeNode(9)
    root2.right.right = TreeNode(7)
    assert solution.findTilt(root2) == 15

    # Test case 3
    root3 = TreeNode(21)
    root3.left = TreeNode(7)
    root3.left.left = TreeNode(1)
    root3.left.right = TreeNode(1)
    root3.left.left.left = TreeNode(3)
    root3.left.left.right = TreeNode(3)
    root3.right = TreeNode(14)
    root3.right.left = TreeNode(2)
    root3.right.right = TreeNode(2)
    assert solution.findTilt(root3) == 9
