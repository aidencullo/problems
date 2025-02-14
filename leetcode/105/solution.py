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
            left_subtree_size = root_index - i_start
            new_p_start_l = p_start + 1
            new_p_end_l = p_start + left_subtree_size
            new_p_start_r = p_start + left_subtree_size + 1
            new_p_end_r = p_end
            new_i_start_l = i_start
            new_i_end_l = root_index - 1
            new_i_start_r = root_index + 1
            new_i_end_r = i_end
            root.left = buildTreeHelper(new_p_start_l, new_p_end_l, new_i_start_l, new_i_end_l)
            root.right = buildTreeHelper(new_p_start_r, new_p_end_r, new_i_start_r, new_i_end_r)
            return root
        hashmap = {val: i for i, val in enumerate(inorder)}
        return buildTreeHelper(0, len(preorder) - 1, 0, len(inorder) - 1)





# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        el = preorder.pop(0)
        i = inorder.index(el)
        left_inorder = inorder[:i]
        right_inoder = inorder[i+1:]
        left_tree_len = len(left_inorder)
        left_preorder = preorder[:left_tree_len]
        right_preorder = preorder[left_tree_len:]
        return TreeNode(
            el, 
            self.buildTree(left_preorder, left_inorder), 
            self.buildTree(right_preorder, right_inoder)
        )
            


