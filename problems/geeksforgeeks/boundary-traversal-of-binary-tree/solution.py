class Node:
    def __init__(self, val, left=None, right=None):
        self.right = right
        self.data = val
        self.left = left


class Solution:

    def printBoundaryView(self, root):
        def isLeaf(node):
            return not node.left and not node.right
        
        def dfs(root):
            if not root:
                return False
            l = dfs(root.left)
            r = dfs(root.right)
            if not l and not r:
                self.traversal.append(root.data)
            return True

        def helper(root):
            if not isLeaf(root):
                self.traversal.append(root.data)

            runner = root.left
            while runner:
                if not isLeaf(runner):
                    self.traversal.append(runner.data)
                runner = runner.left or runner.right

            dfs(root)
            runner = root

            stack = []
            runner = root.right
            while runner:
                if not isLeaf(runner):
                    stack.append(runner.data)
                runner = runner.right or runner.left

            self.traversal.extend(stack[::-1])

        self.traversal = []
        helper(root)
        return self.traversal
