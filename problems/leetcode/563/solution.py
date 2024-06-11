from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.total += abs(left - right)
            return left + right + root.val

        self.total = 0
        dfs(root)
        return self.total
