# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def populate(node, parent_count=0):
            if not node:
                return 0
            counts[node.val] = parent_count
            l = populate(node.left)
            r = populate(node.right, l + 1)
            return l + r + 1

        def populate(node, parent_count=0):
            if not node:
                return 0
            if parent_count == 0:
                parent_count = n - parent_count
            counts[node.val] = 
            r = populate(node.right)
            l = populate(node.left, r + 1)
            return l + r + 1
        
        counts = {}
        populate(root)
        print(counts)
