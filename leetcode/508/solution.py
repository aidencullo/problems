from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            tree_sum = dfs(root.left) + dfs(root.right) + root.val
            tree_sums[tree_sum] += 1
            return tree_sum
        tree_sums = defaultdict(int)
        dfs(root)
        max_freq = max(tree_sums.values(), default=0)
        return [tree_sum for tree_sum, freq in tree_sums.items() if freq == max_freq]
