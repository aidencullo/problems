# time: O(V^2 + V + E)
# space: O(V + E)

from collections import defaultdict
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            if not node in seen:
                seen.add(node)
                for neighbor in graph[node]:
                    dfs(neighbor)
        graph = defaultdict(set)
        for u, neighbors in enumerate(isConnected):
            for v, connected in enumerate(neighbors):
                if connected:
                    graph[u].add(v)
                    graph[v].add(u)
        seen = set()
        provinces = 0
        for vertex in graph:
            if not vertex in seen:
                dfs(vertex)
                provinces += 1
        return provinces
