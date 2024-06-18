from solution import TreeNode, Solution
from collections import deque


def tree_to_list(root):
    """ Helper function to convert tree to list for testing. """
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
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


def test_replaceValueInTree():
    solution = Solution()
    
    # Test case 1
    root = TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(10)), TreeNode(9, None, TreeNode(7)))
    result = solution.replaceValueInTree(root)
    assert tree_to_list(result) == [0, 0, 0, 7, 7, None, 11]
    
    # Test case 2
    root = TreeNode(3, TreeNode(1), TreeNode(2))
    result = solution.replaceValueInTree(root)
    assert tree_to_list(result) == [0, 0, 0]

