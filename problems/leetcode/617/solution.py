from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        cur = TreeNode()
        cur.val = root1.val + root2.val
        cur.left = self.mergeTrees(root1.left, root2.left)
        cur.right = self.mergeTrees(root1.right, root2.right)
        return cur
