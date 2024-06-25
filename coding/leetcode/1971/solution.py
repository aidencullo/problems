class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = {}
        for u, v in edges:
            graph[u] = graph.get(u, []) + [v]
            graph[v] = graph.get(v, []) + [u]
        stack = [source]
        seen = set()
        while stack:
            cur = stack.pop()
            if cur in seen:
                continue
            seen.add(cur)
            if cur == destination:
                return True
            stack.extend(graph[cur])
        return False
