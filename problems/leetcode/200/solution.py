# Solution 1
# O(m * n) time

from typing import Optional, List, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n:
                return 0
            if grid[i][j] != '1':
                return 0
            grid[i][j] = '*'            
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)
            return 1
        
        m = len(grid)
        n = len(grid[0])
        islands = 0
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                islands += dfs(i, j)
        return islands
