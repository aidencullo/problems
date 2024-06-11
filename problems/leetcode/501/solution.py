from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(root: Optional[TreeNode]) -> list[int]:
            if not root:
                return
            dfs(root.left)
            self.inorder.append(root.val)
            dfs(root.right)

        self.inorder = []
        dfs(root)

        mode = 0
        count = 0
        last = None
        self.res = []
        for cur in self.inorder:
            if cur != last:
                count = 1
            else:
                count += 1
            if count == mode:
                self.res.append(cur)
            if count > mode:
                self.res = [cur]
                mode = count
            last = cur
        return self.res
