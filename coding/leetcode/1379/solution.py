class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = []
        while stack or cloned:
            while cloned:
                stack.append(cloned)
                cloned = cloned.left
            cloned = stack.pop()
            if cloned.val == target.val:
                return cloned
            cloned = cloned.right
