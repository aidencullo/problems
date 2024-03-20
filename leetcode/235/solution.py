# Solution for LeetCode problem 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


"""

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

Example 1:

    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8

    Output: 6

    Explanation: The LCA of nodes 2 and 8 is 6.

"""

# O(log n) time and space complexity


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root
