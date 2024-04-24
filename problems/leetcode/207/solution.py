from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node: int):
            if node in visited:
                self.cycle = True
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            graph[node] = set()
            visited.remove(node)

        graph = dict((el, set()) for el in range(numCourses))
        for course, prerequisite in prerequisites:
            graph[course].add(prerequisite)
        visited = set()
        self.cycle = False
        for node in graph:
            dfs(node)
        return not self.cycle
