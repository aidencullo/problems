# # Solution 1

# from collections import deque, defaultdict
# from typing import Optional, List, Tuple

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
#         q = deque()
#         q.append((root, 0))
#         levels_dict = defaultdict(list)
#         while q: # O(n)
#             node, level = q.popleft()
#             levels_dict[level].append(node.val)
#             if node.left:
#                 q.append((node.left, level + 1))
#             if node.right:
#                 q.append((node.right, level + 1))
#         return list(levels_dict.values()) # O(n)







# Solution 2

from collections import deque, defaultdict
from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        result = []
        while q:
            level = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                result.append(level)
        return result
 
