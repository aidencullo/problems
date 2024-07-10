from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        _max = max(nums)
        _idx = nums.index(_max)
        node = TreeNode(_max)
        node.left = self.constructMaximumBinaryTree(nums[:_idx])
        node.right = self.constructMaximumBinaryTree(nums[_idx + 1:])
        return node
