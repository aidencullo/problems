class Solution:
    def bToDLL(self, root):
        def dfs(tail, node):
            if not node:
                return tail
            left_tail = dfs(tail, node.left)
            middle_tail = insert(left_tail, node)
            right_tail = dfs(middle_tail, node.right)
            return right_tail

        def insert(tail, node):
            node.left = tail
            if tail:
                tail.right = node
            return node

        tail = dfs(None, root)
        head = tail
        while head.left:
            head = head.left
        return head
 
