from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        total = 0
        if low <= root.val <= high:
            total += root.val
        return total + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
