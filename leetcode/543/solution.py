# ## Solution 1
# # O(n^2) time O(n) space?
# from typing import Optional

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         root_diameter = longest_path(root.left) + longest_path(root.right)
#         left_diameter = self.diameterOfBinaryTree(root.left)
#         right_diameter = self.diameterOfBinaryTree(root.right)
#         return max((root_diameter, left_diameter, right_diameter))

# def longest_path(node):
#     if not node:
#         return 0
#     return 1 + max(longest_path(node.left), longest_path(node.right))











# ## Solution 2
"""
entirely inspired by another answer i saw, not mine at all
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n) time O(n) space
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diam = 0
        def dfs(node):
            if not node:
                return 0
            right = dfs(node.right)
            left = dfs(node.left)
            self.max_diam = max(self.max_diam, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.max_diam
















# ## Other Solution
# """
# done by someone else
# """
# class Solution:

#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         self.dia = 0  
#         def dfs(root): 
#             if not root: 
#                 return 0 
#             left = dfs(root.left)  # the number of nodes of left subtree longest path 
#             right = dfs(root.right)   # the number of nodes of right subtree longest path 
#             self.dia = max(self.dia, left+right) # right + left + 1, total nodes, minus 1, path length 
#             return max(left, right)+1
#         dfs(root)
#         return self.dia      
