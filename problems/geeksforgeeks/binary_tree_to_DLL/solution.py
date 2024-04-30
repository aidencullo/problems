class Solution:
    def bToDLL(self, root):
        def dfs(node):
            if not node:
                return None

            l = dfs(node.left)
            
            if not l:
                l = node
            else:
                insert_last(l, node)

            r = dfs(node.right)
            insert_right(node, r)
            return l

        def insert_right(node, new_node):
            node.right = new_node
            if new_node:
                new_node.left = node

        def insert_last(node, new_node):
            runner = traverse(node)
            insert_right(runner, new_node)            

        def traverse(node):
            runner = node
            while runner.right:
                runner = runner.right
            return runner

        return dfs(root)
