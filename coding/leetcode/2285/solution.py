class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        graph = {i: 0 for i in range(n)}
        for u, v in roads:
            graph[u] += 1
            graph[v] += 1
        graph = sorted(graph.items(), key=lambda x: x[1])
        return sum((pos + 1) * roads for pos, roads in graph)
