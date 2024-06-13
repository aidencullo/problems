from typing import Optional
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([(root, None)]) if root else deque()

        while q:
            sum_by_parent = defaultdict(int)
            for cur, parent in q:
                sum_by_parent[parent] += cur.val
            total = sum(sum_by_parent.values())
            print(total)
            for i in range(len(q)):
                cur, parent = q.popleft()
                cur.val = total - sum_by_parent[parent]
                if cur.left:
                    q.append((cur.left, cur))
                if cur.right:
                    q.append((cur.right, cur))
        return root
