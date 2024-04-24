from collections import defaultdict
from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node, parent=None):
            if node in visited:
                return visited[visited.index(node):]
            visited.append(node)
            for nb in graph[node]:
                if nb == parent:
                    continue
                cycle = dfs(nb, node)
                if cycle:
                    return cycle
            visited.pop()


        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        self.cycle = []
        visited = []
        for node in graph:
            cycle = dfs(node)
            if cycle:
                self.cycle = cycle
                break
        for u, v in reversed(edges):
            if u in self.cycle and v in self.cycle:
                return [u, v]
