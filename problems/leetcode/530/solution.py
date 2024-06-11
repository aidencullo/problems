from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root: Optional[TreeNode]) -> int:
            if not root:
                return
            inorder(root.left)
            self.diff = min(self.diff, root.val - self.prev)
            self.prev = root.val
            inorder(root.right)
        self.diff = float('inf')
        self.prev = float('-inf')
        inorder(root)
        return self.diff
