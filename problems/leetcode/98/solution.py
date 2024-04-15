import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse_inorder(node: TreeNode):
            if not node:
                return
            traverse_inorder(node.left)
            self.items.append(node.val)
            traverse_inorder(node.right)
        self.items = []
        traverse_inorder(root)
        return (self.items == sorted(self.items)
                and len(self.items) == len(set(self.items)))
