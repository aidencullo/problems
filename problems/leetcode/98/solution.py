# time O(n)
# space O(n)

import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], low: int, high: int) -> None:
            if not node:
                return True
            if node.val < low or node.val > high:
                return False
            return (valid(node.left, low, node.val-1)
                    and valid(node.right, node.val+1, high))
        return valid(root, -math.inf, math.inf)
