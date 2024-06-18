from typing import Optional, List, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(row,  col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if (row, col) in visited:
                return
            visited.add((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc)

        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0':
                    visited.add((row, col))
        for row in range(rows):
            for col in range(cols):
                if not (row, col) in visited:
                    dfs(row, col)
                    islands += 1
        return islands
