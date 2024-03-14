from collections import deque
import math
from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        self.result = []

        while q:
            node, level = q.popleft()
            self.add_to_list(node, level)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return self.result


    def add_to_list(self, node, level):
        val = node.val
        if len(self.result) - 1 == level:
            self.result[level].append(val)
        else:
            self.result.append([])
            self.result[level].append(val)
