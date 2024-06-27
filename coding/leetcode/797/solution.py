from collections import defaultdict


class Solution:
    def allPathsSourceTarget(self, graph_input: list[list[int]]) -> list[list[int]]:
        graph = defaultdict(list)
        for i, nodes in enumerate(graph_input):
            graph[i] = nodes
        src, dest = 0, len(graph) - 1
        stack = [[src]]
        paths = []
        while stack:
            cur = stack.pop()
            if cur[-1] == dest:
                paths.append(cur)
            for node in graph[cur[-1]]:
                stack.append(cur + [node])
        return paths
