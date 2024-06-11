from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(root: Optional[TreeNode]) -> list[int]:
            if not root:
                return
            dfs(root.left)
            if root.val != self.prev:
                self.count = 0
            self.count += 1
            if self.count > self.mode:
                self.res = []
                self.mode = self.count
            if self.count == self.mode:
                self.res.append(root.val)
            self.prev = root.val
            dfs(root.right)

        self.mode = 0
        self.count = 0
        self.prev = None
        self.res = []
        dfs(root)
        return self.res
