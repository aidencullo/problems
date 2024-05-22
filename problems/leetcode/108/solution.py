from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def helper(l, r) -> Optional[TreeNode]:
            if l > r:
                return
            k = (l + r) // 2
            node = TreeNode(nums[k])
            node.left =  helper(l, k - 1)
            node.right = helper(k + 1, r)
            return node
        return helper(0, len(nums) - 1)
