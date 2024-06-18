from solution import Solution, TreeNode




# Test cases for hasPathSum function
def test_has_path_sum():
    solution = Solution()

    # Test case 1
    root1 = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    assert solution.hasPathSum(root1, 22) == True

    # Test case 2
    root2 = build_tree([1,2,3])
    assert solution.hasPathSum(root2, 5) == False

    # Test case 3
    root3 = build_tree([])
    assert solution.hasPathSum(root3, 0) == False

    # Additional test case 4
    root4 = build_tree([1,2])
    assert solution.hasPathSum(root4, 1) == False

    # Additional test case 5
    root5 = build_tree([1,2])
    assert solution.hasPathSum(root5, 3) == True

    # Helper function to build a tree from a list
def build_tree(nodes):
    if not nodes:
        return None
    from collections import deque
    root = TreeNode(nodes[0])
    queue = deque([root])
    index = 1
    while queue and index < len(nodes):
        node = queue.popleft()
        if nodes[index] is not None:
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1
        if index < len(nodes) and nodes[index] is not None:
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1
    return root
