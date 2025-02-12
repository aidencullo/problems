from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], prev) -> bool:
            if not root:
                return
            self.univalue = self.univalue and root.val == prev
            helper(root.left, prev)
            helper(root.right, prev)
        self.univalue = True
        helper(root, root.val)
        return self.univalue
