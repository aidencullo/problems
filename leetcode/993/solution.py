from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def get_node(q, val):
            for node, parent in q:
                if node.val == val:
                    return node, parent
            return None, None
        q = deque([(root, None)])

        while q:
            qlen = len(q)
            x_node, x_parent = get_node(q, x)
            y_node, y_parent = get_node(q, y)
            if x_node and y_node and x_parent != y_parent:
                return True
            for i in range(qlen):
                cur, parent = q.popleft()
                if cur.left:
                    q.append((cur.left, cur))
                if cur.right:
                    q.append((cur.right, cur))
        return False
