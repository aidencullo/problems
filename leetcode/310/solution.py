from typing import List
from collections import defaultdict
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        q = deque()
        degrees = {node: len(graph[node]) for node in graph}
        for node in graph:
            if degrees[node] == 1:
                q.append(node)
        while len(graph) > 2:
            qlen = len(q)
            for _ in range(qlen):
                leaf = q.popleft()
                for parent in graph[leaf]:
                    degrees[parent] -= 1
                    graph[parent].remove(leaf)
                    if degrees[parent] == 1:
                        q.append(parent)
                del graph[leaf]
                del degrees[leaf]
        return list(graph.keys())
