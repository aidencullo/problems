from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> Optional[TreeNode]:
        def helper(l, r) -> Optional[TreeNode]:
            modified_nums = nums[l: r + 1]
            if not modified_nums:
                return
            max_value = max(modified_nums)
            max_index = modified_nums.index(max_value) + l
            node = TreeNode(max_value)
            node.left = helper(l, max_index - 1)
            node.right = helper(max_index + 1, r)
            return node
        return helper(0, len(nums) - 1)
