from collections import deque

from node import Node

def dfs(root: Node):
    visited = []

    def dfs_helper(node: Node):
        if node in visited:
            return
        visited.append(node)
        for neighbor in node.neighbors:
            dfs_helper(neighbor)
    dfs_helper(root)
    return [node.val for node in visited]
