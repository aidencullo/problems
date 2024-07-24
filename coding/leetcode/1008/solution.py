# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        i = 0
        n = len(preorder)
        while i < n and preorder[i] < val:
            i += 1
        root.left = self.bstFromPreorder(preorder[:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
