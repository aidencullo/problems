# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diam(node):
            if not node:
                return 0
            l = diam(node.left)
            r = diam(node.right)
            self.max = max(self.max, l + r)
            return max(l, r) + 1
        self.max = 0
        diam(root)
        return self.max
