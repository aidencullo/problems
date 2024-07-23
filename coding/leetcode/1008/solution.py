# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        val = preorder.pop(0)
        root = TreeNode(val)
        i = 0
        n = len(preorder)
        while i < n and preorder[i] < r
