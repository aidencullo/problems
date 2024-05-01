from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def distance_to_zero(row, col):
            if row < 0 or row >= n or col < 0 or col >= m:
                return float('inf')
            if mat[row][col] == 0:
                return 0
            if (row, col) in visited:
                return float('inf')
            visited.add((row, col))
            min_distance = float('inf')
            for dc, dr in directions:
                min_distance = min(min_distance, distance_to_zero(row + dr, col + dc))
            visited.remove((row, col))
            return min_distance + 1

        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(mat)
        m = len(mat[0])
        updated = [[0] * m for __ in range(n)]
        for row in range(n):
            for col in range(m):
                updated[row][col] = distance_to_zero(row, col)
        return updated
