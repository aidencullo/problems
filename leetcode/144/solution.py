from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return
        yield root.val
        yield from self.preorderTraversal(root.left)
        yield from self.preorderTraversal(root.right)
