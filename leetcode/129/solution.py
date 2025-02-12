# time: O(n)
# space: O(n)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, running):
            if not node:
                return
            current_value = running + node.val
            if not node.left and not node.right:
                self.sum += current_value
                return
            dfs(node.left, current_value * 10)
            dfs(node.right, current_value * 10)
        self.sum = 0
        dfs(root, 0)
        return self.sum
