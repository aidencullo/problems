from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)]
        res = []
        while stack:
            cur, visited = stack.pop()
            if cur and visited:
                res.append(cur.val)
            elif cur and not visited:
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))
        return res
