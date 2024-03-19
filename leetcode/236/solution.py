# Type: Binary Tree
# Difficulty: Medium
# Problem: 236. Lowest Common Ancestor of a Binary Tree
# URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# O(n) time and space

"""

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself)."

Example:

    Input: [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1

    Output: 3

    Explanation: The LCA of nodes 5 and 1 is 3.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        def lowestCommonAncestorHelper(root, p, q):
            if not root:
                return 0
            score = lowestCommonAncestorHelper(root.left, p, q) + lowestCommonAncestorHelper(root.right, p, q)
            if root.val in [p.val, q.val]:
                score += 1
            if score == 2 and not self.lca:
                self.lca = root
            return score
        lowestCommonAncestorHelper(root, p, q)
        return self.lca
