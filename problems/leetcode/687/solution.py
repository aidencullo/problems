class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def longest_path(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            l = longest_path(root.left)
            r = longest_path(root.right)
            if root.left and root.left.val == root.val:
                l += 1
            if root.right and root.right.val == root.val:
                r += 1
            self.max = max(self.max, l + r)
            return max(l, r)
        self.max = 0
        longest_path(root)
        return self.max
