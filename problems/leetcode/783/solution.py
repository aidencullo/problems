from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min_diff = math.inf
        self.prev = -math.inf

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def minDiffInBSTHelper(root: Optional[TreeNode]) -> int:
            if not root:
                return
            minDiffInBSTHelper(root.left)
            self.min_diff = min(self.min_diff, abs(self.prev - root.val))
            self.prev = root.val
            minDiffInBSTHelper(root.right)
        minDiffInBSTHelper(root)
        return self.min_diff
