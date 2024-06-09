from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode], running_sum: int) -> int:
            if not root:
                return False
            current_sum = (running_sum << 1) + root.val
            l = helper(root.left, current_sum)
            r = helper(root.right, current_sum)
            if not l and not r:
                self.total += current_sum
            return True            

        self.total = 0
        helper(root, 0)
        return self.total
