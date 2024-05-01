from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        updated = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    updated.append((i, j, 0))
                    visited.add((i, j))

        while updated:
            for __ in range(len(updated)):
                row, col, distance_to_zero = updated.popleft()
                grid[row][col] = distance_to_zero
                
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if 0 <= new_row < n and 0 <= new_col < m and (new_row, new_col) not in visited:
                        updated.append((new_row, new_col, distance_to_zero + 1))
                        visited.add((new_row, new_col))
        return grid
