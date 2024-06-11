class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode) -> TreeNode:
            if not root:
                return 0
            dfs(root.right)
            root.val += self.prev
            self.prev = root.val
            dfs(root.left)

        self.prev = 0
        dfs(root)
        return root
