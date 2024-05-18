from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        node = root
        res = []
        while stack or node:
            while node:
                stack.append((node, False))
                node = node.left
            node, visited = stack.pop()
            while visited:
                res.append(node.val)
                if not stack:
                    return res
                node, visited = stack.pop()            
            stack.append((node, True))
            node = node.right
        return res
