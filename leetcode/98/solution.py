# linear time and space

import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        min_stack = [-math.inf]
        max_stack = [math.inf]
        current = root
        while current or stack:
            while current:
                stack.append(current)
                max_stack.append(current.val)
                current = current.left
            current = stack.pop()
            max_stack.pop()
            if not (min_stack[-1] < current.val and current.val < max_stack[-1]):
                return False
            min_stack.append(current.val)
            current = current.right
        return True
