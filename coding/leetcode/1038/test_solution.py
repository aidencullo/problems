import pytest
from solution import TreeNode, Solution  # Assuming your file is named solution.py

def tree_to_list(root: TreeNode) -> list:
    """Helper function to convert a binary tree to a list using level-order traversal."""
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

def list_to_tree(lst: list) -> TreeNode:
    """Helper function to convert a list to a binary tree using level-order traversal."""
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    index = 1
    while queue and index < len(lst):
        node = queue.pop(0)
        if node:
            if index < len(lst) and lst[index] is not None:
                node.left = TreeNode(lst[index])
                queue.append(node.left)
            index += 1
            if index < len(lst) and lst[index] is not None:
                node.right = TreeNode(lst[index])
                queue.append(node.right)
            index += 1
    return root

def test_bst_to_gst_case1():
    root = list_to_tree([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8])
    expected_output = [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
    assert tree_to_list(Solution().bstToGst(root)) == expected_output

def test_bst_to_gst_case2():
    root = list_to_tree([0, None, 1])
    expected_output = [1, None, 1]
    assert tree_to_list(Solution().bstToGst(root)) == expected_output

def test_bst_to_gst_single_node():
    root = list_to_tree([5])
    expected_output = [5]
    assert tree_to_list(Solution().bstToGst(root)) == expected_output

def test_bst_to_gst_all_right():
    root = list_to_tree([1, None, 2, None, 3])
    expected_output = [6, None, 5, None, 3]
    assert tree_to_list(Solution().bstToGst(root)) == expected_output

def test_bst_to_gst_all_left():
    root = list_to_tree([3, 2, None, 1])
    expected_output = [3, 5, None, 6]
    assert tree_to_list(Solution().bstToGst(root)) == expected_output

# Add more test cases as needed
