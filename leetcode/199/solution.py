from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        results = []
        q = deque()
        q.append(root)
        while q:
            qlen = len(q)
            for i in range(qlen):
                n = q.popleft()
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            results.append(n.val)
        return results
