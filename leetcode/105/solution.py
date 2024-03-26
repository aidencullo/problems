from typing import List, Optional

# time complexity: O(n^2)
# space complexity: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        left_inorder = inorder[:inorder.index(val)] # O(n)
        right_inorder = inorder[inorder.index(val) + 1:] # O(n)
        left_preorder = preorder[:len(left_inorder)] # O(n)
        right_preorder = preorder[len(left_inorder):] # O(n)
        root.left = self.buildTree(left_preorder, left_inorder) 
        root.right = self.buildTree(right_preorder, right_inorder)
        return root
