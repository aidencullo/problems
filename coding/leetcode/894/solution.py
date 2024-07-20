from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> list[Optional[TreeNode]]:
        trees = []
        root = TreeNode(0)
        for i in range(1, n, 2):
            for left in self.allPossibleFBT(i):
                for right in self.allPossibleFBT(n - 1 - i):
                    root.left = left
                    root.right = right
                    tree.append(root)
        return trees
