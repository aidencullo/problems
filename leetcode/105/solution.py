# from typing import List, Optional

# Solution 1: using list slicing
# # time complexity: O(n^2)
# # space complexity: O(n)

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder:
#             return None
#         val = preorder.pop(0)
#         root = TreeNode(val)
#         left_inorder = inorder[:inorder.index(val)] # O(n)
#         right_inorder = inorder[inorder.index(val) + 1:] # O(n)
#         left_preorder = preorder[:len(left_inorder)] # O(n)
#         right_preorder = preorder[len(left_inorder):] # O(n)
#         root.left = self.buildTree(left_preorder, left_inorder) 
#         root.right = self.buildTree(right_preorder, right_inorder)
#         return root



# Solution 2: using hashmap to store inorder index
# time complexity: O(n)
# space complexity: O(n)
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTreeHelper(p_start, p_end, i_start, i_end) -> Optional[TreeNode]:
            if p_start > p_end:
                return None
            root = TreeNode(preorder[p_start])
            root_index = hashmap[preorder[p_start]]
            root.left = buildTreeHelper(p_start + 1, p_start + 1 + (root_index-i_start) - 1, i_start, root_index-1)
            root.right = buildTreeHelper(p_start + 1 + (root_index-i_start), p_end, root_index+1, i_end)
            return root
        hashmap = {val: i for i, val in enumerate(inorder)}
        return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)
