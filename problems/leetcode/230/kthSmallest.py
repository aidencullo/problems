# time: O(n)
# space: O(n)

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order(root: Optional[TreeNode]) -> List[int]:
            if root:
                in_order(root.left)
                self.items.append(root.val)
                in_order(root.right)
        self.items = []
        in_order(root)
        return self.items[k-1]
