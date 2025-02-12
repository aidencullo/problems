from typing import Optional
from collections import deque
from itertools import groupby
from operator import itemgetter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def get_first(obj):
            return obj[0]

        def get_second(obj):
            return obj[1]

        q = deque([(root, None)]) if root else deque()

        while q:
            parent_child = list((parent, child.val) for child, parent in q)
            grouped = groupby(
                parent_child,
                key=itemgetter(0)
            )
            sum_by_parent = {
                key: sum(value for _, value in group)
                for key, group
                in grouped
            }
            total = sum(sum_by_parent.values())
            for i in range(len(q)):
                cur, parent = q.popleft()
                cur.val = total - sum_by_parent[parent]
                if cur.left:
                    q.append((cur.left, cur))
                if cur.right:
                    q.append((cur.right, cur))
        return root
