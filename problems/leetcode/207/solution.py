from typing import Optional, List, Tuple
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_dict = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            course_dict[course].append(prereq)

        visit_set = set()
        def dfs(node):
            if course_dict[node] == []:
                return True
            if node in visit_set:
                return False
            visit_set.add(node)
            for nb in course_dict[node]:
                if not dfs(nb): return False
            visit_set.remove(node)
            course_dict[node] = []
            return True
        for course in course_dict:
            if not dfs(course): return False
        return True
