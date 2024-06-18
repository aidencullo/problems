class Solution:
    def bToDLL(self, root):
        def dfs(node):
            if not node:
                return

            dfs(node.left)

            nonlocal head, tail
            if tail:
                tail.right = node
                node.left = tail
                tail = node
            if not head:
                head = tail = node

            dfs(node.right)
            
        head = tail = None
        dfs(root)
        return head
