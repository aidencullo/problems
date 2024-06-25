# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(g, p, root: TreeNode) -> int:
            if not root:
                return
            if g and g % 2 == 0:
                self.res += root.val
            dfs(p, root.val, root.left)
            dfs(p, root.val, root.right)
        self.res = 0
        dfs(None, None, root)
        return self.res
