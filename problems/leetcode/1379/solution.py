class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = []
        while stack or original:
            while original:
                stack.append(cloned)
                stack.append(original)
                cloned = cloned.left
                original = original.left
            original = stack.pop()
            cloned = stack.pop()
            if original == target:
                return cloned
            original = original.right
            cloned = cloned.right
