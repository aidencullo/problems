from solution import Solution
import pytest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

# Test cases for deepestLeavesSum function
def test_deepest_leaves_sum():
    solution = Solution()

    # Test case 1
    root1 = build_tree([1,2,3,4,5,None,6,7,None,None,None,None,8])
    assert solution.deepestLeavesSum(root1) == 15

    # Test case 2
    root2 = build_tree([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5])
    assert solution.deepestLeavesSum(root2) == 19

    # Test case 3
    root3 = build_tree([1])
    assert solution.deepestLeavesSum(root3) == 1

    # Additional test case 4
    root4 = build_tree([1,2,3,4,None,None,5,None,6,None,None,None,7])
    assert solution.deepestLeavesSum(root4) == 13

    # Additional test case 5
    root5 = build_tree([7,4,3,None,None,2,None,1])
    assert solution.deepestLeavesSum(root5) == 1

if __name__ == "__main__":
    pytest.main()
