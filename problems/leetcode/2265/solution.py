import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(root: TreeNode) -> int:
            if not root:
                return 0, 0
            left, n = dfs(root.left)
            right, m = dfs(root.right)
            if math.floor((left + right + root.val) / (n + m + 1)) == root.val:
                self.result += 1
            return root.val + left + right, n + m + 1
        self.result = 0
        dfs(root)
        return self.result
