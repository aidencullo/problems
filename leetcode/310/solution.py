# time: O(V + E)
# space: O(V + E)

from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        leaves = deque()
        degrees = {node: len(graph[node]) for node in graph}
        for node in degrees:
            if degrees[node] == 1:
                leaves.append(node)
        while n > 2:
            n -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                parent = graph[leaf].pop()
                degrees[parent] -= 1
                graph[parent].remove(leaf)
                if degrees[parent] == 1:
                    new_leaves.append(parent)
            leaves = new_leaves
        return list(leaves)
