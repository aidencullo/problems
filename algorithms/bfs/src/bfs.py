from collections import deque

from node import Node

def bfs(node: Node):
    visited = []
    q = deque()

    def bfs_helper(node: Node):
        q.append(node)

        while q:
            current = q.popleft()
            if current not in visited:
                visited.append(current)
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    q.append(neighbor)
    bfs_helper(node)
    return [node.val for node in visited]
    
