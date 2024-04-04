# Time: O(n) for timsort
# space: O(n)

import math
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.vals = set()
        stack = [root]
        while stack:
            node = stack.pop()
            self.vals.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        if len(self.vals) == 1:
            return -1
        return sorted(list(self.vals))[1]
