# O((logn)^2) time and O(logn) space

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root, val):
            if not root:
                return False
            if root.val == val:
                return True
            return search(root.left, val) or search(root.right, val)
        if root.val == q.val or root.val == p.val:
            return root
        search_q_left = search(root.left, q.val)
        if search_q_left:
            if search_p_right:
                return root
            return self.lowestCommonAncestor(root.left, p, q)
        if search_p_right:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
