# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidBSTHelper(lower, upper, root):
            if not root:
                return True
            return (lower < root.val
                    and root.val < upper
                    and isValidBSTHelper(lower, root.val, root.left)
                    and isValidBSTHelper(root.val, upper, root.right))
        return isValidBSTHelper(float('-inf'), float('inf'), root)
