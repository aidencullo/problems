# # Solution 1

# # time: O(n)
# # space: O(n)

# from typing import Optional, List

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         def in_order(root: Optional[TreeNode]) -> List[int]:
#             if root:
#                 in_order(root.left)
#                 self.items.append(root.val)
#                 in_order(root.right)
#         self.items = []
#         in_order(root)
#         return self.items[k-1]




# # Solution 2

# # time: O(n)
# # space: O(log(n))


# from typing import Optional, List

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:

#     def __init__(self):
#         self.i = 0
#         self.res = 0

#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         def dfs(node: Optional[TreeNode]):
#             if not node:
#                 return
#             dfs(node.left)
#             self.i += 1
#             if k == self.i:
#                 self.res = node.val
#             dfs(node.right)
#         dfs(root)
#         return self.res






# Solution 3

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
