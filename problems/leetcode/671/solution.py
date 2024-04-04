# time: O(n)
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
        def dfs(node):
            if not node.left:
                return math.inf
            l = node.left.val
            r = node.right.val
            if node.val == node.left.val:
                l = dfs(node.left)
            if node.val == node.right.val:
                r = dfs(node.right)
            return min(l, r)
        second_min = dfs(root)
        if second_min == math.inf:
            return -1
        return second_min
