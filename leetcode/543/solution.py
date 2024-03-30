from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# time: O(n)
# space: O(n)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diam(node):
            if not node:
                return 0
            l = diam(node.left)
            r = diam(node.right)
            self.longest = max(self.longest, l + r)
            return max(l, r) + 1
        self.longest = 0
        diam(root)
        return self.longest
