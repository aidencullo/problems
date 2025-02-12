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
        i = bisect.bisect_right(preorder, val)
        root.left = self.bstFromPreorder(preorder[:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
