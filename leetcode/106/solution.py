from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def buildTreeHelper(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            if not inorder:
                return None
            current_val = postorder.pop()
            root = TreeNode(current_val)
            root_index = inorder.index(current_val)
            root.right = buildTreeHelper(inorder[root_index + 1:], postorder)
            root.left = buildTreeHelper(inorder[:root_index], postorder)
            return root
        return buildTreeHelper(inorder, postorder)
        
