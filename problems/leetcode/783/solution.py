from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(root: Optional[TreeNode]) -> list[int]:
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        traversed = inorder(root)
        res = [abs(a - b) for a, b in zip(traversed[1:], traversed)]
        return min(res)
