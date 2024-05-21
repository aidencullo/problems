from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)
                for child in cur.children or []:
                    q.append(child)
            res.append(level)
        return res
