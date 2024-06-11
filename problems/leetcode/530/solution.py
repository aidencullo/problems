class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], low, high) -> int:
            if not root:
                return
            self.diff = min(
                self.diff,
                abs(high - root.val),
                abs(low - root.val)
            )
            dfs(root.left, low, root.val)
            dfs(root.right, root.val, high)
        self.diff = float('inf')
        dfs(root, float('-inf'), float('inf'))
        return self.diff
