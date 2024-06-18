class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        l = self.increasingBST(root.left)
        r = self.increasingBST(root.right)
        head = l or root
        if l:
            while l.right:
                l = l.right
            l.right = root
        root.right = r
        root.left = None
        return head
     

"""
order?
unique?
size constraints?
empty tree?
negative values?


APPROACH

while node or stack
    a. repeat until None hit
        1. push cur node
        2. move to left child
    b. pop from stack
    c. process node
    d. move to right child
"""
