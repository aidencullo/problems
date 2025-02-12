class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def insert(arr):
            if not arr:
                return
            val = arr[len(arr) // 2]
            node = TreeNode(val)
            node.left = insert(arr[:len(arr) // 2])
            node.right = insert(arr[len(arr) // 2 + 1:])
            return node

        def traverse(root: TreeNode) -> TreeNode:
            if not root:
                return
            traverse(root.left)
            inorder.append(root.val)
            traverse(root.right)

        inorder = []
        traverse(root)
        median = inorder[len(inorder) // 2]
        return insert(inorder)
