from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        def helper(root: Optional[TreeNode], path: str) -> list[str]:
            if not root:
                return
            if not root.left and not root.right:
                self.paths.append(path + str(root.val))
            path += str(root.val) + "->"
            helper(root.left, path)
            helper(root.right, path)
        self.paths = []
        helper(root, "")
        return self.paths
