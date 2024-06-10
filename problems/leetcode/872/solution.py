from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeafs(root1) == self.getLeafs(root2)

    def getLeafs(self, root1: Optional[TreeNode]) -> list[int]:
        def helper(root1: Optional[TreeNode]) -> list[int]:
            if not root1:
                return
            if not root1.left and not root1.right:
                leaves.append(root1.val)
            helper(root1.left)
            helper(root1.right)
            
        leaves = []
        helper(root1)
        return leaves
