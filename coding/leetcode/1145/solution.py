# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def count_nodes(node):
            if not node:
                return 0
            l = count_nodes(node.left)
            r = count_nodes(node.right)
            if node.val == x:
                m = max(l, r, n - (l + r + 1))
                self.winner = m > n - m                
            return 1 + l + r

        self.winner = False
        count_nodes(root)
        return self.winner
