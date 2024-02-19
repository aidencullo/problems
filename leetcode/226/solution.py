from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __repr__(self):
    #     items = []
    #     d = deque()
    #     d.append(self)
    #     while len(d):
    #         node = d.popleft()
    #         items.append(node.val)
    #         if node.left:
    #             d.append(node.left)
    #         if node.right:
    #             d.append(node.right)
    #     return str(items)

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

# ## implementing a solution i saw
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         d = collections.deque()
        
#         if root:
#            d.append(root)

#         while d:
#             node = d.popleft()
#             node.left, node.right = node.right, node.left
#             if node.left:
#                 d.append(node.left)
#             if node.right:
#                 d.append(node.right)
#         return root
