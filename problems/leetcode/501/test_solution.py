from solution import TreeNode, Solution  # Assuming your file is named solution.py

def test_find_mode_single_element():
    root = TreeNode(0)
    assert Solution().findMode(root) == [0]

def test_find_mode_multiple_elements_single_mode():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)
    assert Solution().findMode(root) == [2]

def test_find_mode_multiple_elements_multiple_modes():
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(2)
    result = Solution().findMode(root)
    assert set(result) == {1, 2}

def test_find_mode_all_elements_same():
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    assert Solution().findMode(root) == [2]

def test_find_mode_complex_tree():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(5)
    result = Solution().findMode(root)
    assert set(result) == {2, 5}

# Add more test cases as needed
