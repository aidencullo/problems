from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                if node.left and node.right:
                    stack.append(node.right)
                node = node.left or node.right
            node = stack.pop()
            while True:
                res.append(node.val)
                child = node
                node = stack.pop() if stack else None
                if not node or not child in [node.right, node.left]:
                    break
        return res
