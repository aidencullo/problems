class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        node = root
        stack = []
        head = TreeNode()
        runner = head
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            runner.right = TreeNode(node.val)
            runner = runner.right
            node = node.right
        return head.right

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
