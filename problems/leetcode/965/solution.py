from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode]) -> bool:
            if not root:
                return 
            l = helper(root.left)
            r = helper(root.right)
            if not l is None:
                self.univalue = self.univalue and root.val == root.left.val
            if not r is None:
                self.univalue = self.univalue and root.val == root.right.val
            return root.val
        self.univalue = True
        helper(root)
        return self.univalue
