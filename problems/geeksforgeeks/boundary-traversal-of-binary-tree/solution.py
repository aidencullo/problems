class Node:
    def __init__(self, val, left=None, right=None):
        self.right = right
        self.data = val
        self.left = left


class Solution:

    def printBoundaryView(self, root):
        def dfs(root):
            if not root:
                return False
            l = dfs(root.left)
            r = dfs(root.right)
            if not l and not r:
                self.traversal.append(root.data)
            return True

        def helper(root):
            runner = root
            while runner.left or runner.right:
                self.traversal.append(runner.data)
                runner = runner.left or runner.right
            if runner.right:
                self.traversal.append(runner.data)

            dfs(root)
            runner = root

            stack = []
            runner = root
            while runner.right or runner.left:
                stack.append(runner.data)
                runner = runner.right or runner.left
            if runner.left:
                stack.append(runner.data)

            self.traversal.extend(stack[::-1])

        self.traversal = []
        helper(root)
        return self.traversal[:-1]
