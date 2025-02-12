from solution import TreeNode, Solution


def tree_to_list(root):
    """Helper function to convert binary tree to list representation."""
    if not root:
        return []
    result = []
    queue = [root]
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


def test_all_possible_fbt():
    sol = Solution()

    # Test case 1
    n = 7
    result = sol.allPossibleFBT(n)
    expected = [
        [0, 0, 0, None, None, 0, 0, None, None, 0, 0],
        [0, 0, 0, None, None, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, None, None, None, None, 0, 0],
        [0, 0, 0, 0, 0, None, None, 0, 0]
    ]
    assert len(result) == len(expected)
    for tree in result:
        assert tree_to_list(tree) in expected

    # Test case 2
    n = 3
    result = sol.allPossibleFBT(n)
    expected = [[0, 0, 0]]
    assert len(result) == len(expected)
    for tree in result:
        assert tree_to_list(tree) in expected
