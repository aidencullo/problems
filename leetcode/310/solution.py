# time: O(V + E)
# space: O(V + E)

from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(set) # O(1)
        for v1, v2 in edges: # O(E)
            graph[v1].add(v2) # O(1)
            graph[v2].add(v1) # O(1)
        q = deque()
        degrees = {node: len(graph[node]) for node in graph} # O(V)
        for node in graph: # O(V)
            if degrees[node] == 1:
                q.append(node) # O(1)
        while len(graph) > 2:
            qlen = len(q)
            for _ in range(qlen):
                leaf = q.popleft()
                for parent in graph[leaf]:
                    degrees[parent] -= 1
                    graph[parent].remove(leaf) # O(1)
                    if degrees[parent] == 1:
                        q.append(parent) # O(1)
                del graph[leaf] # O(1)
                del degrees[leaf] # O(1)
        return list(graph.keys()) # O(V)
