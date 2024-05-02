from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def visit(node):
            if node in visited:
                return
            visited.add(node)
            for room in rooms[node]:
                visit(room)
        visited = set()
        visit(0)
        return len(visited) == len(rooms)
