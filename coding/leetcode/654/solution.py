from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> Optional[TreeNode]:
        def helper(low: int, high: int):
            if low > high:
                return
            cur_arr = nums[low: high + 1]
            max_val = max(cur_arr)
            max_idx = low + cur_arr.index(max_val)
            node = TreeNode(max_val)
            node.left = helper(low, max_idx - 1)
            node.right = helper(max_idx + 1, high)
            return node
        return helper(0, len(nums) - 1)
