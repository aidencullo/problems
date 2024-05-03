from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node):
            visited.add(node)
            child_labels = [0] * 26
            for child in graph[node]:
                if child in visited:
                    continue
                new_labels = dfs(child)
                child_labels = [a + b for a, b in zip(child_labels, new_labels)]
            child_labels[ord(labels[node]) % 26] += 1
            res[node] = child_labels[ord(labels[node]) % 26]
            return child_labels
        
        graph = dict((node, []) for node in range(n))
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = [0] * n
        visited = set()
        dfs(0)
        return res
