class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        graph = {i: [0, 0] for i in range(1, n + 1)}
        for a, b in trust:
            graph[a][0] += 1
            graph[b][1] += 1
        for i, (in_degree, out_degree) in enumerate(graph.values(), 1):
            if in_degree == 0 and out_degree == n - 1:
                return i
        return -1
