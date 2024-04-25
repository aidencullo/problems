from collections import defaultdict
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node, parent=None):
            if node in visited:
                self.cycle = visited[visited.index(node):]
                return True
            visited.append(node)
            for nb in graph[node]:
                if nb == parent:
                    continue
                if dfs(nb, node):
                    return True
            visited.pop()
            return False

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        self.cycle = []
        visited = []
        for node in graph:
            if dfs(node):
                break

        for u, v in reversed(edges):
            if u in self.cycle and v in self.cycle:
                return [u, v]
