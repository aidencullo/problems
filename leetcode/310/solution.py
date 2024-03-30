from typing import List
from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def height(node): # O(V + E)
            def dfs(node):
                if node in seen:
                    return 0
                seen.append(node)
                return max((dfs(c) for c in graph[node])) + 1
            seen.append(node)
            return max((dfs(c) for c in graph[node]))
        if n == 1:
            return [0]

        graph = defaultdict(list)
        for v1, v2 in edges: # O(E)
            graph[v1].append(v2)
            graph[v2].append(v1)
        heights = {}
        seen = []
        for node in graph: # O(V)
            heights[node] = height(node)
            seen.clear()
        min_height = min(heights.values()) # O(V)
        return [node for node in heights if heights[node] == min_height] # O(V)
