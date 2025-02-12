from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root: Optional[TreeNode]) -> bool:
            if not root:
                return False
            if k - root.val in hashset:
                return True
            hashset.add(root.val)
            return dfs(root.left) or dfs(root.right)
        hashset = set()
        return dfs(root)
