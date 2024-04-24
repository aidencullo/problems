from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node: int):
            if node in cycle:
                return False
            if node in visited:
                return True

            cycle.add(node)
            for nb in graph[node]:
                if not dfs(nb):
                    return False
            cycle.remove(node)
            visited.add(node)
            order.append(node)
            return True

        graph = dict((el, []) for el in range(numCourses))
        for src, dest in prerequisites:
            graph[src].append(dest)
            
        order = []
        cycle, visited = set(), set()
        for node in graph:
            if not dfs(node):
                return []
        return order
