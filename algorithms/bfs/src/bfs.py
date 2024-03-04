from collections import deque

from node import Node

def bfs(root: Node):
    visited = []
    q = deque()

    def bfs_helper(root: Node):
        visited.append(root)
        q.append(root)

        while q:
            current = q.popleft()
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.append(neighbor)
    bfs_helper(root)
    return [node.val for node in visited]
    
